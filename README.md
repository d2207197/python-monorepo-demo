# Python Monorepo Demo

This repository demonstrates a Python monorepo structure using Poetry for packaging and dependency management.

## Structure

- **`apps/`**: Contains applications. Applications should not import other applications.
- **`libs/`**: Contains libraries. Applications can import multiple libraries.

## Getting Started

1. **Install Poetry**: Follow the [Poetry installation guide](https://python-poetry.org/docs/#installation) to install Poetry.
2. Refer to the README in `apps/be-funny/` and follow the installation instructions.
3. Review the structure and `pyproject.toml` in `libs/` to understand dependency management.
4. Examine the `pyproject.toml` in `apps/be-funny/` to understand script definitions and dependency management.

## Guidelines
### Applications

- Split an application into multiple applications only if necessary, such as when multiple services are highly unrelated and managed by different teams.
- Applications must not be imported by other applications or libraries.
- Each application may include a `Dockerfile` for containerization. While not shown in this repository, it is a common practice in production environments.
- Define Python dependencies in the root `pyproject.toml` file. The `Dockerfile` should manage only non-Python dependencies, except for Python itself, Poetry, and pip.

### Libraries

- Libraries are required when multiple applications need to use the same functionality. Usually, it's originally a package or module under one original application.
- Libraries are located in the `libs/` directory and can be imported by both applications and other libraries.
- Libraries should not contain a `Dockerfile`. All dependencies must be managed through the `pyproject.toml` file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.