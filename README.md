# simple-cookiecutter

A Cookiecutter template for quickly setting up a modern Python project with best practices.

## What does this Cookiecutter do?

This template scaffolds a new Python project with a standardized structure, including:

- Source code and package directory
- Data, tests, documentation, scripts, and notebooks folders
- Pre-configured `pyproject.toml` for Poetry
- Optional integration with tools like pytest, black, mypy, and flake8

You can customize the project name, package name, description, and which development tools to include.

## Project Structure

A generated project will look like this:

```
your_project_name/
├── your_package_name/
├── data/
├── docs/
├── notebooks/
├── results/
├── scripts/
├── tests/
├── .gitignore
├── LICENSE
├── README.md
└── pyproject.toml
```

## How to use this Cookiecutter

### Prerequisites

- [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/):  
    Install with `pip install cookiecutter`
- [Poetry](https://python-poetry.org/):  
    Install with `pip install poetry`

### Usage

```bash
# Generate a new project from this template
cookiecutter gh:your-username/simple-cookiecutter
```

You will be prompted for project details and tool preferences.

### Next steps

1. Navigate into your new project directory.
2. Install dependencies:

    ```bash
    poetry install
    ```

3. Start developing your project!

## License

This template is licensed under the MIT License - see the LICENSE file for details.
