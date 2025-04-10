#!/bin/bash
# Script to create the basic package structure

# Create main package directory if it doesn't exist
mkdir -p aether

# Create subpackages
mkdir -p aether/core
mkdir -p aether/tokenizers
mkdir -p aether/parsers
mkdir -p aether/models
mkdir -p aether/metrics
mkdir -p aether/visualization
mkdir -p aether/utils

# Create __init__.py files
touch aether/__init__.py
touch aether/core/__init__.py
touch aether/tokenizers/__init__.py
touch aether/parsers/__init__.py
touch aether/models/__init__.py
touch aether/metrics/__init__.py
touch aether/visualization/__init__.py
touch aether/utils/__init__.py

# Create tests directory
mkdir -p tests
touch tests/__init__.py

# Copy existing files to the correct locations (if they exist)
if [ -f __init__.py ]; then
  cp __init__.py aether/
fi

if [ -f __version__.py ]; then
  cp __version__.py aether/
fi

if [ -f cli.py ]; then
  cp cli.py aether/
fi

echo "Basic package structure created successfully."
echo "You can now try installing the package with: pip install -e ."
