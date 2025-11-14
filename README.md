# simple-cookiecutter

A modern Cookiecutter template for quickly setting up professional Python projects with uv, testing, and CI/CD best practices. This template creates a complete Python project with organized directories, uv configuration, optional development tools (pytest, black, mypy, flake8), GitHub Actions CI/CD, and automatic project initialization.

## Prerequisites

Before using this template, ensure you have the following installed:

### Required Dependencies
- **Python 3.8+** - The template supports Python 3.8 and newer
- **Cookiecutter** - Template engine for project scaffolding
  ```bash
  pip install cookiecutter
  ```
- **uv** - Modern Python package and project manager
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

### Optional Dependencies
- **Git** - Version control (recommended) - [Install Git](https://git-scm.com/)

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
| `project_short_description` | Brief project description | "A Python project using uv" |
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

### Python Version Selection

When prompted for the `python_version`, you must specify your target Python version with a comparison operator:

| Format | Example | Description |
|--------|---------|-------------|
| **Exact version** | `==3.10.5` | Specifies an exact Python version |
| **Patch version range** | `==3.11.*` | Any patch version of Python 3.11 (e.g., 3.11.0, 3.11.1, 3.11.8) |
| **Greater than or equal** | `>=3.10` | Python 3.10 or newer |
| **Greater than** | `>3.9` | Python 3.10 and newer (excludes 3.9) |

The selected Python version will be used in:
- `pyproject.toml` - Sets the required Python version constraint
- `.github/workflows/ci.yml` - Specifies the Python version for CI/CD testing
- Type checking configurations (MyPy)

### Example Session

```bash
$ cookiecutter gh:RDoerfel/simple-cookiecutter
project_name [My Python Project]: Data Analysis Toolkit
project_slug [data-analysis-toolkit]: 
package_name [data_analysis_toolkit]: 
project_short_description [A Python project using uv]: A comprehensive toolkit for data analysis and visualization
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
└── pyproject.toml                  # Project configuration
```

## Post-Generation Setup

After generating your project, the template will offer to:

1. **Initialize Git repository** with initial commit
2. **Install dependencies** using uv

### Manual Setup (if automated setup was skipped)

```bash
# Navigate to your project
cd your-project-name

# Initialize git (if not done automatically)
git init
git add .
git commit -m "Initial commit"

# Install dependencies
uv sync
```

## Development Workflow

### Running Tests
```bash
# Run all tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=your_package_name

# Generate HTML coverage report
uv run pytest --cov=your_package_name --cov-report=html
```

### Code Quality
```bash
# Format code with Black
uv run black .

# Type checking with MyPy
uv run mypy your_package_name/

# Linting with Flake8
uv run flake8 your_package_name/ tests/
```

### Adding Dependencies
```bash
# Add runtime dependency
uv add pandas numpy

# Add development dependency
uv add --dev jupyter ipython

# Update dependencies
uv sync
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

## Acknowledgments

- [Cookiecutter](https://cookiecutter.readthedocs.io/) - The template engine
- [uv](https://docs.astral.sh/uv/) - Fast Python package and project manager
- [pytest](https://pytest.org/) - Testing framework
- [Black](https://black.readthedocs.io/) - Code formatter
- [MyPy](https://mypy.readthedocs.io/) - Static type checker