# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

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

## License

This project is licensed under the MIT License - see the LICENSE file for details.