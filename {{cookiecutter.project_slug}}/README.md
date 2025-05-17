# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}
{% if cookiecutter.use_github_actions == 'y' -%}

[![CI](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/workflows/CI/badge.svg)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/actions?query=workflow%3ACI)
{% if cookiecutter.use_coverage == 'y' -%}
[![codecov](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}})
{% endif -%}
{% endif -%}

## Project Structure

```
├── src/                # Source code
│   └── {{cookiecutter.package_name}}/
├── data/               # Data files
├── tests/              # Test files
├── docs/               # Documentation
├── scripts/            # Utility scripts
├── notebooks/          # Jupyter notebooks
└── pyproject.toml      # Poetry configuration
```

## Installation

```bash
# Install the package and dependencies
poetry install
```

## Usage

```python
from {{cookiecutter.package_name}} import some_function
```

## Development

### Setting up the development environment

```bash
# Install all dependencies including development dependencies
poetry install
```

{% if cookiecutter.use_pytest == 'y' -%}
### Testing

```bash
# Run tests
poetry run pytest
```
{% endif -%}

{% if cookiecutter.use_coverage == 'y' -%}
### Code Coverage

```bash
# Run tests with coverage
poetry run pytest --cov=src/{{cookiecutter.package_name}} --cov-report=html

# View the HTML coverage report
open htmlcov/index.html  # On macOS
# xdg-open htmlcov/index.html  # On Linux
# start htmlcov/index.html  # On Windows
```
{% endif -%}

{% if cookiecutter.use_black == 'y' -%}
### Formatting

```bash
# Format the code
poetry run black .
```
{% endif -%}

{% if cookiecutter.use_mypy == 'y' -%}
### Type checking

```bash
# Run type checking
poetry run mypy src/ tests/
```
{% endif -%}

{% if cookiecutter.use_flake8 == 'y' -%}
### Linting

```bash
# Run linting
poetry run flake8 src/ tests/
```
{% endif -%}

{% if cookiecutter.use_github_actions == 'y' -%}
## Continuous Integration

This project uses GitHub Actions for continuous integration. The following checks are run on each push and pull request to the main branch:

{% if cookiecutter.use_black == 'y' -%}
- Code formatting with Black
{% endif -%}
{% if cookiecutter.use_flake8 == 'y' -%}
- Linting with Flake8
{% endif -%}
{% if cookiecutter.use_mypy == 'y' -%}
- Type checking with MyPy
{% endif -%}
{% if cookiecutter.use_pytest == 'y' -%}
- Running tests with pytest
{% endif -%}
{% if cookiecutter.use_coverage == 'y' -%}
- Code coverage reporting with pytest-cov and Codecov
{% endif -%}
{% endif -%}

## License

This project is licensed under the MIT License - see the LICENSE file for details.
