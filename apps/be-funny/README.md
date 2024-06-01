# Be Funny

This is a demo application that demonstrates the use of various tools and libraries to manage dependencies and implement a CLI interface. Below are the steps to set up and use the application.

## Features
- Dependency management with Poetry.
- Local libraries under `../../libs` are used.
- CLI interface implemented using Click, accessible via the `be-funny` command.
- Can be imported as a Python package.

## Cross-package Dependencies
- `libs/modeling`
- `libs/processing`

## Setup

### Check Python Environment
Ensure you have the correct Python version by running:

```console
python --version
```
Check the Python executable path:
```console
python -c 'import sys; print(sys.executable)'
```

### Create Virtual Environment
Create and activate a virtual environment:

```console
python -m venv .venv
source .venv/bin/activate
pip install -U pip
python -c 'import sys; print(sys.executable)' # Verify Python executable is under .venv
```

### Install the Application
For end users, install using pip:

```console
pip install apps/be-funny
```


For developers, install using Poetry to handle dependencies:
```console
poetry install
```


## Usage

### Invoke CLI Interface
Access help for the CLI:

```console
be-funny --help
python -m be_funny.cli --help # Equivalent to the above
be-funny create-dataset --help
```

### Import in Python
Start Python and import the application:

```console
python
>>> import be_funny
```
