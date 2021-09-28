# Python api tests

[![Build Status](https://app.travis-ci.com/Roophina/api_tests_home_work.svg?branch=master)](https://app.travis-ci.com/Roophina/api_tests_home_work)

This is a tutorial project that shows how to implement api tests in Python

The project uses:
1. Python
2. Requests
3. CI


Testing application (write with Flask):

git: https://github.com/berpress/flask-restful-api

url: https://stores-tests-api.herokuapp.com


###How to start

Use python 3.8 +

Create and activate virtual environments

```
python3 -m venv env
source env/bin/activate
```

Run in terminal

```
pip install -r requirements.txt
```

or install poetry https://python-poetry.org/, then

```
poetry install
```

and add pre-commit
```
pre-commit install
```

###Run all tests

```python
pytest
```
