# Contributing to Æther

Thank you for considering contributing to Æther! This document provides guidelines and instructions for contributing to the project.

## Development Environment

### Prerequisites

- Python 3.10 or higher
- Conda 10.7 or higher (recommended for environment management)
- Git

### Setting Up Your Environment

1. Fork and clone the repository

```bash
git clone https://github.com/yourusername/aether.git
cd aether
```

2. Create and activate a virtual environment.

Using conda

```bash
conda env create -f environment.yml
conda activate aether
```

Or using pip/venv

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

# Install in development mode
pip install -e ".[dev]"
```

3. Install pre-commit hooks:

```bash
pre-commit install
```

## Coding Standards

- We follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) with some modifications as defined in our configuration files.
- Maximum line length is 88 characters (as enforced by Black).
- Use docstrings for all public modules, functions, classes, and methods.
- Write tests for all new functionality.

## Git Workflow

1. Create a new branch for your feature of bugfix:

```bash
git checkout -b feature/your-feature-name

# or
git checkout -b fix/issue-number-description
```

2. Make your changes and commit them:

```bash
git add .
git commit -m "<type>(<scope>): <description>"
```

3. Push your branch to GitHub:

```bash
git push origin feature/your-feature-name
```

4. Submit a pull request to the main repository

## Pull Request Process

1. Ensure your code adheres to the coding standards and passes all tests.
2. Update documentation if necessary.
3. Add yourself to `CONTRIBUTORS.md` if you're not already listed.
4. The PR should be reviewd by at least one other contributor.

## Testing

- Write unit tests for all new functionality.
- Run tests before submitting a PR:

```bash
pytest
```

## Documentation

- Update any relevant documentation when making changes.
- Follow the docstring format used in the project.

## Code of Conduct

Please adhere to the project's code of conduct in all interactions.

---

Thank you contributing to Æther!
