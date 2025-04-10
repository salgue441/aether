# Installation Guide

This guide will walk you through installing Æther on your system. Æther supports multiple installation methods to fit your workflow.

## Prerequisites

Before installing Æther, ensure you have the following prerequisites:

- Python 3.10 or higher
- Git
- Conda 10.7 or higher (optional, but recommended for environment management)

## Installation Methods

### Using Pip

The simplest way to install Æther is using pip:

```bash
# Clone the repository
git clone https://github.com/salgue441/aether.git
cd aether

# Install using pip
pip install .

# Or for development mode with extras
pip install -e ".[dev]"  # Development tools
pip install -e ".[ml]"   # Machine learning extras
pip install -e ".[viz]"  # Visualization extras
pip install -e ".[dev,ml,viz]"  # All extras
```

### Using Conda

If you prefer using conda for environment management:

```bash
# Clone the repository
git clone https://github.com/salgue441/aether.git
cd aether

# Create and activate a conda environment
conda env create -f environment.yml
conda activate aether

# Install the package in development mode
pip install -e .
```

### Manual Installation

If you need more control over the installation process:

```bash
# Clone the repository
git clone https://github.com/salgue441/aether.git
cd aether

# Install the core dependencies
pip install numpy scikit-learn torch tree-sitter matplotlib networkx fasttext click tqdm pygments jinja2 transformers

# Install development dependencies (optional)
pip install pytest pytest-cov black isort mypy flake8
```

## Verifying Installation

To verify that Æther has been installed correctly, run:

```bash
aether --version
```

You should see the current version of Æther printed to the console.

## Installing Tree-sitter Grammars

Æther requires language-specific grammars for AST parsing. These should be automatically installed, but if you encounter issues:

```bash
# From the aether directory
python -m aether.parsers.setup_grammars
```

## Docker Installation

For a containerized installation:

```bash
# Build the Docker image
docker build -t aether .

# Run Æther from the container
docker run aether compare --help
```

Or using docker-compose:

```bash
# Start the development environment
docker-compose run dev
```

## Troubleshooting

### Common Issues

#### Missing Dependencies

If you encounter errors about missing dependencies:

```bash
pip install -e ".[dev,ml,viz]"
```

#### Permission Issues

If you encounter permission issues:

```bash
# On Unix-like systems
sudo pip install .

# Or install for the current user only
pip install --user .
```

#### GPU Support

To enable GPU support for machine learning models:

```bash
# Install PyTorch with CUDA support
pip install torch --extra-index-url https://download.pytorch.org/whl/cu117
```

### Getting Help

If you encounter any problems during installation, please:

1. Check the [GitHub Issues](https://github.com/salgue441/aether/issues) for similar problems
2. Consult the [Troubleshooting Guide](troubleshooting.md)
3. Open a new issue if your problem hasn't been addressed

## Next Steps

Now that you have Æther installed, check out the [Quickstart Guide](quickstart.md) to begin using the tool.
