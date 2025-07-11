#!/usr/bin/env python
import shutil
import subprocess
from pathlib import Path


def initialize_git():
    """Initialize git repository."""
    subprocess.run(["git", "init"], check=True)
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)
    print("Git repository initialized with initial commit.")


def initialize_pyenv():
    """Initialize pyenv and select Python version."""
    python_version = "{{ cookiecutter.python_version }}"
    subprocess.run(["poetry", "env", "use", python_version], check=True)


def initialize_poetry():
    """Initialize poetry and install dependencies."""
    subprocess.run(["poetry", "install"], check=True)
    print("Poetry dependencies installed.")


def create_gitkeep_files():
    """Create .gitkeep files in empty directories to ensure they are tracked by git."""
    empty_dirs = ["data", "docs", "scripts", "notebooks"]
    for dir_name in empty_dirs:
        gitkeep_file = Path(dir_name) / ".gitkeep"
        if not gitkeep_file.exists():
            with open(gitkeep_file, "w") as f:
                pass
    print("Created .gitkeep files in empty directories.")


def cleanup_github_files():
    """Remove GitHub-related files if GitHub Actions is not enabled."""
    use_github_actions = "{{ cookiecutter.use_github_actions }}"
    if use_github_actions.lower() != "y":
        github_dir = Path(".github")
        if github_dir.exists():
            shutil.rmtree(github_dir)
            print("Removed .github directory since GitHub Actions is not enabled.")


def main():
    try:
        create_gitkeep_files()
        cleanup_github_files()
        print("Would you like to initialize a git repository? (y/n)")
        choice = input().lower()
        if choice == "y":
            initialize_git()
        print("Would you like to select the python version using pyenv? (y/n)")
        choice = input().lower()
        if choice == "y":
            initialize_pyenv()
        print("Would you like to install dependencies now? (y/n)")
        choice = input().lower()
        if choice == "y":
            initialize_poetry()
    except Exception as e:
        print(f"An error occurred: {e}")
        print("You may need to run these commands manually.")


if __name__ == "__main__":
    main()
