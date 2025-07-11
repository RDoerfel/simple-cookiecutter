# simple-cookiecutter

A modern Cookiecutter template for quickly setting up professional Python projects with Poetry, testing, and CI/CD best practices. This template creates a complete Python project with organized directories, Poetry configuration, optional development tools (pytest, black, mypy, flake8), GitHub Actions CI/CD, and automatic project initialization.

## Prerequisites

Before using this template, ensure you have the following installed:

### Required Dependencies
- **Python 3.8+** - The template supports Python 3.8 and newer
- **Cookiecutter** - Template engine for project scaffolding
  ```bash
  pip install cookiecutter
  ```
- **Poetry** - Modern Python dependency management
  ```bash
  pip install poetry
  ```

### Optional Dependencies
- **Git** - Version control (recommended) - [Install Git](https://git-scm.com/)
- **pyenv** - Python version management (optional but recommended) - [Install pyenv](https://pyenv.net/)

## Usage

### Quick Start

```bash
# Generate a new project from this template
cookiecutter gh:RDoerfel/simple-cookiecutter
```

### Configuration Options

During project generation, you'll be prompted for:

| Option | Description | Default |
|--------|-------------|---------|
| `project_name` | Human-readable project name | "My Python Project" |
| `project_slug` | URL-friendly project name (auto-generated) | "my-python-project" |
| `package_name` | Python package name (auto-generated) | "my_python_project" |
| `project_short_description` | Brief project description | "A Python project using Poetry" |
| `python_version` | Target Python version | "3.10" |
| `author_name` | Your full name | "Your Name" |
| `author_email` | Your email address | "your.email@example.com" |
| `github_username` | Your GitHub username | "yourusername" |
| `use_pytest` | Include pytest for testing | "y" |
| `use_coverage` | Include coverage reporting | "y" |
| `use_black` | Include Black code formatter | "y" |
| `use_mypy` | Include MyPy type checker | "y" |
| `use_flake8` | Include Flake8 linter | "y" |
| `use_github_actions` | Include GitHub Actions CI/CD | "y" |

### Example Session

```bash
$ cookiecutter gh:RDoerfel/simple-cookiecutter
project_name [My Python Project]: Data Analysis Toolkit
project_slug [data-analysis-toolkit]: 
package_name [data_analysis_toolkit]: 
project_short_description [A Python project using Poetry]: A comprehensive toolkit for data analysis and visualization
python_version [3.10]: 3.11
author_name [Your Name]: Jane Smith
author_email [your.email@example.com]: jane.smith@example.com
github_username [yourusername]: janesmith
use_pytest [y]: 
use_coverage [y]: 
use_black [y]: 
use_mypy [y]: 
use_flake8 [y]: 
use_github_actions [y]: 
```
## Generated Project Structure

```
data-analysis-toolkit/
├── data_analysis_toolkit/          # Main source package
│   └── __init__.py
├── data/                           # Data files
│   └── .gitkeep
├── docs/                           # Documentation
│   └── .gitkeep
├── notebooks/                      # Jupyter notebooks
│   └── .gitkeep
├── results/                        # Analysis results
│   └── .gitkeep
├── scripts/                        # Utility scripts
│   └── .gitkeep
├── tests/                          # Test files
│   ├── __init__.py
│   └── .gitkeep
├── .github/                        # GitHub Actions (if enabled)
│   └── workflows/
│       └── ci.yml
├── .gitignore                      # Git ignore rules
├── LICENSE                         # MIT License
├── README.md                       # Project documentation
└── pyproject.toml                  # Poetry configuration
```

## Post-Generation Setup

After generating your project, the template will offer to:

1. **Initialize Git repository** with initial commit
2. **Set up Python environment** using pyenv (if available)
3. **Install dependencies** using Poetry

### Manual Setup (if automated setup was skipped)

```bash
# Navigate to your project
cd your-project-name

# Initialize git (if not done automatically)
git init
git add .
git commit -m "Initial commit"

# Set Python version (if using pyenv)
pyenv local 3.11  # or your chosen version

# Install dependencies
poetry install

# Activate virtual environment
poetry shell
```

## Development Workflow

### Running Tests
```bash
# Run all tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov=your_package_name

# Generate HTML coverage report
poetry run pytest --cov=your_package_name --cov-report=html
```

### Code Quality
```bash
# Format code with Black
poetry run black .

# Type checking with MyPy
poetry run mypy your_package_name/

# Linting with Flake8
poetry run flake8 your_package_name/ tests/
```

### Adding Dependencies
```bash
# Add runtime dependency
poetry add requests pandas numpy

# Add development dependency
poetry add --group dev jupyter ipython

# Update dependencies
poetry update
```

## GitHub Integration

When GitHub Actions is enabled, the template creates a complete CI/CD pipeline that:

- Runs on every push and pull request to main branch
- Tests code formatting with Black
- Performs linting with Flake8
- Runs type checking with MyPy
- Executes test suite with pytest
- Reports coverage to Codecov
- Supports multiple Python versions (configurable)

### Setting up Codecov (Optional)

1. Visit [codecov.io](https://codecov.io) and connect your GitHub repository
2. Copy the upload token from your repository settings
3. Add it as a secret named `CODECOV_TOKEN` in your GitHub repository settings

**Python version not found**: Install the required Python version
```bash
# Using pyenv
pyenv install 3.11.0
pyenv global 3.11.0

# Or update python_version in cookiecutter.json
```

## Acknowledgments

- [Cookiecutter](https://cookiecutter.readthedocs.io/) - The template engine
- [Poetry](https://python-poetry.org/) - Modern Python dependency management
- [pytest](https://pytest.org/) - Testing framework
- [Black](https://black.readthedocs.io/) - Code formatter
- [MyPy](https://mypy.readthedocs.io/) - Static type checker