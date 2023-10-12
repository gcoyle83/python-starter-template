[![](https://github.com/gcoyle83/python-starter-template/actions/workflows/checks.yml/badge.svg?branch=main)](https://github.com/gcoyle83/python-starter-template/actions/workflows/checks.yml)
[![Docs](https://github.com/gcoyle83/python-starter-template/actions/workflows/render_docs.yml/badge.svg)](https://github.com/gcoyle83/python-starter-template/actions/workflows/render_docs.yml)

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

For usage details, see the project [website](https://gcoyle83.github.io/python-starter-template).

# Documentation
Another critical component of any well-developed Python project is, of course, documentation. For this template, the documentation is *written/edited* in the `write_docs` directory and is rendered into a website in the `docs` folder during the (semi-automatic) build process.

For documentation details, including how to edit documentation and generate a website, see the [Documentation tools](https://gcoyle83.github.io/python-starter-template/tools/documentation.html) page.
