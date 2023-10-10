![Python Starter Template](https://github.com/noahgift/github-actions-pytest/workflows/Python%20application%20test%20with%20Github%20Actions/badge.svg)

# Python Starter Template
This repo provides a basic starter template for best practices developing and testing Python code, including: 

-  Virtual environment management with `venv`
-  Code formatting and linting with `Pylint` and `Black`
-  Build and unit tests with Makefile and `Pytest`
-  Continuous integration via GitHub Actions

> Note, many of the concepts implemented here are directly from the excellent Duke University Coursera Course by Noah Gift: [*Cloud Computing Foundations*](https://coursera.org/share/0e44a583040b010e6aeb674febbac00e)

# Usage

> This repo is a *template*. DO NOT clone it and then attempt to modify it (this will fail by design).

## Create a new repo from this template
Start a new GitHub repo, and select this repo from the "Repository Template" option. Be sure to select the subsequent "Include all branches" option to benefit from the project documentation, website and GitHub Pages branches. The remainder of the usage instructions assume that actions are taken from this new repository.

## Create virtual environment
The next step is to build the virtual environment for this project locally, as follows:

1. First, note that the project "requires" (by way of declaration right here), use of Python 3.12; since `venv` uses whatever Python interpreter calls it as the base, we need to be sure that we call `venv` with Python 3.12 as the active interpreter. To do so:
    -  Install Python 3.12 from [python.org](https://www.python.org/downloads/)
    -  Keep all defaults when running the installer, noting the installation location should be at `C:\Users\<user>\AppData\Local\Programs\Python\Python312`
    -  Close the installer app when it is finished
    -  Open a Bash (or Powershell) terminal
    -  Enter command `C:\Users\<user>\AppData\Local\Programs\Python\Python312\python -m venv .venv` to create a virtual environment in a subdirectory named `.venv`
        -  Running the `python -m venv` command from the directory where Python 3.12 is forces use of the 3.12 interpreter as base
        -  Specifying the `.venv` directory to create the virtual environment in follows standard practice and ensures that these files are ignored by git (as indicated in the `.gitignore` file in the "Environments" section) 
    -  Open the `.venv` folder and then the `pyvenv.cfg` file; note that the Python `version` is 3.12.x

1. Next, add the required packages to this virtual environment:

    -  First, activate the environment by running 
        -  (PowerShell) `.venv/Scripts/Activate.ps1`
        -  (Bash) `.venv/Scripts/activate`
    -  Install requirements with `pip install -r requirements.txt`

## Unit tests with `Pytest`
1. Now run the test suite in `test_hello.py` with the command `python -m pytest -vv test_hello.py`. Note the result (passing coverage) printed to the terminal
1. Now use `black` to format your Python code to PEP 8 compliance (Black is an opinionated strict subset of PEP 8):

    -  First, open `hello.py` and paste the following function into the end of the module:
        ```
        def my_func(x):
            """
            This is my function it returns the product of `x` and `a`
            """
            a = [
                1,2,3
            ]
            return a*x
        ```
    -  Now run the command `black *.py`, and open `hello.py` again. Note the input has been reformatted to:
        ```
        def my_func(x):
            """
            This is my function it returns the product of `x` and `a`
            """
            a = [1, 2, 3]
            return a * x
        ```
    