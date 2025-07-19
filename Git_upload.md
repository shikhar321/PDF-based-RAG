# Instructions to upload from VS Code to Github
1. Make sure repo is alrady created and empty
1. Create a git ignore file (Used Gemini Extension on VS Code)

1. commit: git add . 
    1. git status`
    1. git commit -m "commit_msg"
    settings->developer settings->tokens(classic)->tick all->generate token
    git remote add origin https://shikhar321:<GIT_PAT_TOKEN>@github.com/shikhar321/RAG-PDF
    git push
