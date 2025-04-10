#!/bin/bash
# Script to initialize the project structure

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}Initializing Æther project structure...${NC}"

# Create main package directories
echo -e "${YELLOW}Creating package directories...${NC}"
mkdir -p aether/{core,tokenizers,parsers,models,metrics,visualization,cli,utils}
mkdir -p tests/{core,tokenizers,parsers,models,metrics,visualization,cli,utils}
mkdir -p docs/{api,examples,guides}

# Create __init__.py files
echo -e "${YELLOW}Creating __init__.py files...${NC}"
touch aether/__init__.py
touch aether/{core,tokenizers,parsers,models,metrics,visualization,cli,utils}/__init__.py
touch tests/__init__.py
touch tests/{core,tokenizers,parsers,models,metrics,visualization,cli,utils}/__init__.py

# Create example test
echo -e "${YELLOW}Creating an example test...${NC}"
cat >tests/test_basic.py <<'EOF'
"""Basic test to ensure testing setup works."""

def test_import():
    """Test that the package can be imported."""
    import aether
    assert aether is not None

def test_version():
    """Test that the package has a version."""
    from aether import __version__
    assert __version__ is not None
EOF

# Create basic CLI module
echo -e "${YELLOW}Creating basic CLI module...${NC}"
cat >aether/cli.py <<'EOF'
"""Command-line interface for Æther."""

import click

@click.group()
@click.version_option()
def main():
    """Æther - Advanced source code similarity detection."""
    pass

@main.command()
@click.argument('file1', type=click.Path(exists=True))
@click.argument('file2', type=click.Path(exists=True))
@click.option('--threshold', '-t', default=0.75, help='Similarity threshold (0.0 to 1.0)')
@click.option('--format', '-f', default='text', help='Output format (text, json, html)')
def compare(file1, file2, threshold, format):
    """Compare two source code files for similarity."""
    click.echo(f"Comparing {file1} and {file2} with threshold {threshold} and format {format}")
    # Placeholder for actual comparison logic
    click.echo("Similarity: 0.0 (placeholder)")

if __name__ == '__main__':
    main()
EOF

# Create version file
echo -e "${YELLOW}Creating version file...${NC}"
cat >aether/__version__.py <<'EOF'
"""Version information."""

__version__ = "0.1.0"
EOF

# Update main __init__.py
cat >aether/__init__.py <<'EOF'
"""Æther - Advanced source code similarity detection system."""

from aether.__version__ import __version__

__all__ = ["__version__"]
EOF

# Create data directories
echo -e "${YELLOW}Creating data directories...${NC}"
mkdir -p data/{raw,processed,external,interim}
touch data/{raw,processed,external,interim}/.gitkeep

# Create models directory
echo -e "${YELLOW}Creating models directory...${NC}"
mkdir -p models
touch models/.gitkeep

# Create examples directory
echo -e "${YELLOW}Creating examples directory...${NC}"
mkdir -p examples/{source,target}

# Setup complete
echo -e "${GREEN}Project structure initialized successfully!${NC}"
echo -e "Next steps:"
echo -e "  1. Install dependencies: ${YELLOW}pip install -e \".[dev]\"${NC}"
echo -e "  2. Initialize git: ${YELLOW}git init${NC}"
echo -e "  3. Run tests: ${YELLOW}pytest${NC}"
