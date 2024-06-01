# A demo of Python monorepo

- Use poetry for packaging and dependency management
- `apps/` for applications. Applications shouldn't import other applications.
- `libs/` for library. Applications can import libraries.

Check the README under `apps/be-funny/`



# Python Monorepo Demo

This repository demonstrates a Python monorepo structure using Poetry for packaging and dependency management.

## Structure

- **`apps/`**: Contains applications. Applications should not import other applications.
- **`libs/`**: Contains libraries. Applications can import multiple libraries.

## Getting Started

1. **Install Poetry**: Follow the [Poetry installation guide](https://python-poetry.org/docs/#installation) to install Poetry.
2. Check the README under `apps/be-funny/` for more details.

## Applications

For more details on individual applications, check the README under each application's directory. For example, see the README under `apps/be-funny/`.

## Libraries

Libraries are located in the `libs/` directory and can be imported by applications as needed.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.