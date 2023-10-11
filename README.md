[![Remote tests](https://github.com/gcoyle83/python-starter-template/actions/workflows/checks.yml/badge.svg?branch=main)](https://github.com/gcoyle83/python-starter-template/actions/workflows/checks.yml)
# Python Starter Template
This repo provides a basic starter template for best practices developing and testing *unpackaged* Python code. Emphasis on that last point - this is **not** a Python packaging template. This template is for use with generic Python projects that want to take advantage of automated tools to improve the development process, including: 

-  Virtual environment management with `venv`
-  Code formatting and linting with `Pylint` and `Black`
-  Functional tests with `Pytest`
-  Remote tests to support reproducibility (via GitHub Actions)

If you are looking for a template repo for Python projects that will be distributed as packaged libraries, [maybe we should create one](https://packaging.python.org/en/latest/overview/)...

> [!NOTE]  
> Many of the concepts implemented here are directly from the excellent Duke University Coursera Course by Noah Gift: [*Cloud Computing Foundations*](https://coursera.org/share/0e44a583040b010e6aeb674febbac00e)

# Usage

> [!WARNING]  
> This repo is a *template*. DO NOT clone it and then attempt to modify it (this will fail by design).

For usage details, see the [Usage](docs/01_Usage.md) documentation.

# Documentation
Another critical component of any well-developed Python project is, of course, documentation. For this template, the documentation is kept in the `docs` directory and is developed using Markdown and Quarto.

For documentation details, including how to set up to edit documentation and generate a project website, see [Documentation](docs/02_Documentation.md) and [GitHub Pages](docs/03_GithubPages.md), respectively.
