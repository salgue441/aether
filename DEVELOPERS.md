# Developer Documentation for Æther

This document provides technical information for developers working on the Æther codebase.

## Architecture Overview

Æther is structured as a modular Python package that combines multiple techniques for code similarity detection:

```
aether/
├── core/               # Core functionality and base classes
├── tokenizers/         # Code tokenization for different languages
├── parsers/            # AST generation and processing
├── models/             # ML models for code similarity detection
├── metrics/            # Similarity metrics implementation
├── visualization/      # Result visualization tools
├── cli/                # Command-line interface
└── utils/              # Utility functions and helpers
```

## Development Workflow

### Branch Strategy

- `main`: Production-ready code
- `develop`: Integration branch for features
- `feature/*`: New features
- `fix/*`: Bug fixes
- `release/*`: Release preparation

### Code Review Process

1. Create an issue describing the feature/bug
2. Implement your changes in a feature/fix branch
3. Submit a PR to the `develop` branch
4. Address review comments
5. Squash and merge to `develop`

### Testing Strategy

- Unit tests: Test individual components in isolation
- Integration tests: Test interaction between components
- Functional tests: Test end-to-end functionality
- Property-based tests: For complex algorithms

## Performance Considerations

- Use vectorized operations with NumPy where possible
- Consider memory usage when processing large codebases
- For computationally intensive tasks, use multiprocessing
- Cache intermediate results when appropriate

## Documentation Guidelines

- Use Google-style docstrings
- Document all public APIs
- Include examples for complex functionality
- Update documentation when interfaces change

## Benchmarking

When making performance improvements:

1. Establish a baseline with current code
2. Make your changes and measure impact
3. Document performance changes in PR

## Environment Management

Create new environments with:

```bash
# Using conda
conda env create -f environment.yml

# Using pip
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -e ".[dev]"
```

## Debugging Tips

- Use `logging` module instead of print statements
- VSCode launch configurations are provided in `.vscode/launch.json`
- Set `PYTHONPATH` to include the project root for easier imports
- Use pytest's `--pdb` flag to debug failing tests

## Code Generation

Some code in this project might be auto-generated. Look for comments indicating generated code and don't modify these sections directly.

## Advanced Development Topics

### Custom Tree-sitter Parsers

To add support for a new language:

1. Add a tree-sitter grammar to `parsers/grammars/`
2. Implement a language-specific AST converter
3. Register the new language in `parsers/__init__.py`

### ML Model Training

Models are trained with:

```bash
python -m aether.models.train --config path/to/config.toml
```

## Security Considerations

- Never commit sensitive data or credentials
- Validate all user inputs, especially file paths
- Use secure hashing algorithms when appropriate
- Be cautious with dynamic code execution
