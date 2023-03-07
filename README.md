# Movie Project

This is a basic project to learn how to use `peewee` and create some basic unit tests in python.


Setup
----------

Create a virtual environment:

```shell
   python3 -m venv venv
```


#### Activate virtual environment

MacOS and Linux:
```shell
  source venv/bin/activate
```

Windows cmd:
```shell
  venv\Scripts\activate.bat
```

Windows Powershell:
```shell
  venv\Scripts\Activate.ps1
```

Install and update using `pip`:
```shell
  pip install -r requirements.txt
```


Running Locally
----------------

```shell
  python main.py
```

Testing
--------

Run tests with `pytest`:

```shell
  pytest -v
```

Run tests with `coverage`:

```shell
  coverage run -m pytest
```

Coverage report:
```shell
  coverage report
```
