.. image:: https://github.com/gcoyle83/python-starter-template/actions/workflows/checks.yml/badge.svg?branch=main
    :target: https://github.com/pylint-dev/pylint/actions
# Python Starter Template
This repo provides a basic starter template for best practices developing and testing *unpackaged* Python code. Emphasis on that last point - this is **not** a Python packaging template. This template is for use with generic Python projects that want to take advantage of automated tools to improve the development process, including: 

-  Virtual environment management with `venv`
-  Code formatting and linting with `Pylint` and `Black`
-  Functional tests with `Pytest`
-  Remote tests to support reproducibility (via GitHub Actions) with Makefile

If you are looking for a template repo for Python projects that will be distributed as packaged libraries, [maybe we should create one](https://packaging.python.org/en/latest/overview/)...

> Note, many of the concepts implemented here are directly from the excellent Duke University Coursera Course by Noah Gift: [*Cloud Computing Foundations*](https://coursera.org/share/0e44a583040b010e6aeb674febbac00e)

# Usage

> This repo is a *template*. DO NOT clone it and then attempt to modify it (this will fail by design).

## Create a new repo from this template
Start a new GitHub repo, and select this repo from the "Repository Template" option. Be sure to select the subsequent "Include all branches" option to benefit from the project documentation, website and GitHub Pages branches. The remainder of the usage instructions assume that actions are taken from this new repository.

## Create virtual environment
The next step is to build the virtual environment for this project locally, as follows:

1. First, note that the project "requires" (by way of declaration right here), use of Python 3.12; since `venv` uses whatever Python interpreter calls it as the base, each user needs to be sure to call `venv` with Python 3.12 as the active interpreter. To do so:
    -  Install Python 3.12 from [python.org](https://www.python.org/downloads/)
    -  Keep all defaults when running the installer, noting the installation location should be at `C:\Users\<user>\AppData\Local\Programs\Python\Python312`
    -  Close the installer app when it is finished
    -  Open a Bash (or Powershell) terminal
    -  Enter command `C:\Users\<user>\AppData\Local\Programs\Python\Python312\python -m venv .venv` to create a virtual environment in a subdirectory named `.venv`
        -  Running the `python -m venv` command from the directory where Python 3.12 is stored forces use of the 3.12 interpreter as base
        -  Creating the virtual environment in the `.venv` directory follows standard practice and ensures that these files are ignored by git (as indicated in the `.gitignore` file in the "Environments" section) 
    -  Open the `.venv` folder and then the `pyvenv.cfg` file; note that the Python `version` is 3.12.x

1. Next, add the required packages to this virtual environment:

    -  First, activate the environment by running 
        -  (PowerShell) `.venv/Scripts/Activate.ps1`
        -  (Bash) `.venv/Scripts/activate`
    -  Install requirements with `pip install -r requirements.txt`

## Automatic linting and formatting with `Pylint` and `black`
It is important but tedious to follow formatting standards. Automated tools have been developed by those who agree with this statement (starting at Bell Labs almost 50 years ago. A [linter](https://en.wikipedia.org/wiki/Lint_(software)) is a tool for static code analysis used to flag programming errors, bugs, stylistic errors and suspicious constructs. [Pylint](https://pylint.readthedocs.io/en/stable/) is one such tool that is widely used for Python. [Black](https://black.readthedocs.io/en/stable/the_black_code_style/index.html) is another, and these two tools are [often used in parallel](https://pylint.readthedocs.io/en/latest/?badge=latest#advised-linters-alongside-pylint) to get the most benefit. The following steps will help you understand how to use these tools to improve your Python projects:

1. Use `Pylint` to analyze the code in the `src` folder:
    ```
    pylint src
    ```
    This command will analyze all `*.py` files in the `src` folder. Note that the output to the terminal includes recommendations to include docstrings for modules and functions, and another recommendation to improve efficiency of the `python_version` function in `version.py`. 
    
    None of these recommendations are compliance issues, and they can be suppressed. Note the overall score is 4.62/10. Suppressing these recommendations with the `--disable` flag:
    ```
    pylint --disable=R,C src
    ``` 
    > Note, `--disable=R,C` indicates that 'refactor' and 'convention' messages should be disabled
    The resulting output should now have no suggestions, and the overall rating is 10/10

    Finally, only errors can be reported by passing the `--errors-only` flag
    ```
    pylint --errors-only src
    ```
    Note that know rating is returned. Try introducing an error into a module and run again to see what happens.

1. Now use `black` to format your Python code to PEP 8 compliance ([Black]() is an opinionated strict subset of PEP 8). While `Pylint` can be used to generate a set of recommendations or flag errors, `Black` can be used to automatically enforce formatting conventions:

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
    -  Now run the command `black src`, and open `hello.py` again. Note the input has been reformatted to:
        ```
        def my_func(x):
            """
            This is my function it returns the product of `x` and `a`
            """
            a = [1, 2, 3]
            return a * x
        ```
By using first `Black` and then `Pylint` to flag remaining errors after automatic reformatting, much of the tedium of code review can be avoided.
## Unit tests with `Pytest`
After static review, the code can be dynamically tested. The [`Pytest`](https://docs.pytest.org/en/7.4.x/index.html) package is designed to facilitate testing of Python projects from basic unit tests to full evaluation of functional requirements for complex projects. Here it is used to enable and demonstrate basic unit testing.

1. Run the test suite in the `tests` directory with the command `python -m pytest -vv tests`. 
1. Note the results (percent complete and pass/fail status) printed to the terminal after each functional unit test.

## Remote testing
Testing on the development system is a fundamental first step, but Python projects should also be regularly tested on remote systems to ensure that they can be shared without issue. The GitHub Workflow file `checks.yml` enables an automated workflow to run the above steps (build Python environment, format and lint code, run tests) on a remote GitHub "runner". 
