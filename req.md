### .venv file to separate requirement from global python (only first time before starting project)

python -m venv .venv
.\.venv\Scripts\Activate.ps1

# If working with python notebook ipynb file, make sure kernel is set to .venv interpreter
# Choose this by clicking on right corner

# Install all libraries from text file in one go
pip install -r requirements.txt
