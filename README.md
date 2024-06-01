# Python Monorepo Demo

This repository demonstrates a Python monorepo structure using Poetry for packaging and dependency management.

## Structure

- **`apps/`**: Contains applications. Applications should not import other applications.
- **`libs/`**: Contains libraries. Applications can import multiple libraries.

## Getting Started

1. **Install Poetry**: Follow the [Poetry installation guide](https://python-poetry.org/docs/#installation) to install Poetry.
2. Check the README under `apps/be-funny/` and follow the installation instructions.
3. Check the structure and `pyproject.toml` under `libs/` to understand how dependencies work.
4. Check the `pyproject.toml` under `apps/be-funny/` to understand how scripts are defined, and dependencies are managed.

## Guidelines
### Applications

- Applications must not be imported by other applications or libraries.
- Each application may include a `Dockerfile` for containerization. Although not shown in this repository, it is a common practice in production environments.
- Define Python dependencies in the root `pyproject.toml` file. The `Dockerfile` should only manage non-Python dependencies, with the exception of Python itself, Poetry, and pip.

### Libraries

- Libraries are located in the `libs/` directory and can be imported by both applications and other libraries.
- Libraries should not contain a `Dockerfile`. All dependencies must be managed through the `pyproject.toml` file.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.