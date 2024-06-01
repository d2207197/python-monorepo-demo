# Be Funny

Dependencies
- `libs/modeling`
- `libs/processing`

Check python environment
```console
$ python --version
$ python -c 'import sys; print(sys.executable)'
```

Create virtual environment
```console
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -U pip
$ python -c 'import sys; print(sys.executable)'  # check if the Python executable is under .venv
```

Install the be-funny package. Use pip or poetry.
```console
$ pip install apps/be-funny # with pip for production
$ poetry install            # with poetry for development
```

Invoke CLI interface
```console
$ be-funny --help
$ python -m be_funny.cli --help  # the same as the above
$ be-funny create-dataset --help
```

Import in Python
```console
$ python
>>> import be_funny
```