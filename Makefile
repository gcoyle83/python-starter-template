install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black src
	black tests

lint:
	pylint --disable=R,C hello.py

test:
	python -m pytest -vv tests

all: install format lint test
