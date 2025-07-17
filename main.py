# pip install langchain
# pip install langchain_community
# pip install langchain-google-genai
# pip install langchain_experimental
# pip install sentence-transformers
# pip install langchain_chroma
# pip install langchainhub
# pip install pypdf
# pip install rapidocr-onnxruntime

# Run this file on online jupyter notebook as running on local system "Kernal Crashed"
# error is encountered

import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# For this script to work, you'll need to install the following packages:
# pip install langchain langchain-community langchain-google-genai langchain-text-splitters chromadb pypdf python-dotenv

# You also need a .env file in the same directory with your Google API key:
# GOOGLE_API_KEY="your_google_api_key_here"

# Load environment variables
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables. Please create a .env file with the key.")

# 1. Load document
print("Loading document...")
loader = PyPDFLoader(r"data\GenAi Notes.pdf")
data = loader.load()
print("Document loaded.")

# 2. Split data into chunks
print("Splitting document into chunks...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = text_splitter.split_documents(data)
print(f"Total numbers of documents after splitting: {len(docs)}")

# 3. Create embeddings and store in vector database
print("Creating embeddings and vector store...")
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)
vectorstore = Chroma.from_documents(documents=docs, embedding=embeddings)
print("Vector store created.")

# 4. Create a retriever
# 5 means we will fetch out 5 documents which are most similar to our answer to query
retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

# 5. Define the LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", google_api_key=api_key, temperature=0.3)

# 6. Create a RAG prompt template
template = """You are a helpful assistant. Answer the question based only on the following context:

{context}

Question: {question}

Answer:"""
prompt = ChatPromptTemplate.from_template(template)

# 7. Create the RAG chain using LangChain Expression Language (LCEL)
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# 8. Ask a question
question = "What are the key concepts of Generative AI?"
print(f"\nInvoking RAG chain with question: '{question}'")
response = rag_chain.invoke(question)
print("\nAnswer:\n", response)