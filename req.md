### .venv file to separate requirement from global python (only first time before starting project)

python -m venv .venv
.\.venv\Scripts\Activate.ps1

### rq.txt file contains all the libraries needed to run the project
# We can install all the libraries in one go

# If working with python notebook ipynb file, make sure kernel is set to .venv interpreter
# choose this by clicking on right corner

# https://youtu.be/hH4WkgILUD4?si=NoZJAlsY4URtsts6


# Install libraries from text file
pip install -r requirements.txt



