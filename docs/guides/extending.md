# Extending Æther

This guide explains how to extend and customize Æther for your specific needs. Æther is designed with extensibility in mind, allowing you to add new languages, detection methods, and output formats.

## Architecture Overview

Before extending Æther, it's helpful to understand its architecture:

```
aether/
├── core/         # Core functionality
├── tokenizers/   # Language-specific tokenization
├── parsers/      # AST generation and processing
├── models/       # ML models for similarity detection
├── metrics/      # Similarity measurement algorithms
├── visualization/ # Report generation
├── cli/          # Command-line interface
└── utils/        # Helper functions
```

Each component follows a plugin-based architecture with base classes that can be extended.

## Adding Support for a New Language

### 1. Create a Tokenizer

First, create a new tokenizer for your language:

```python
# aether/tokenizers/rust_tokenizer.py
from aether.tokenizers.base import BaseTokenizer

class RustTokenizer(BaseTokenizer):
    """Tokenizer for Rust programming language."""

    @property
    def language(self) -> str:
        return "rust"

    @property
    def file_extensions(self) -> list[str]:
        return [".rs"]

    def tokenize(self, code: str) -> list[str]:
        """Tokenize Rust code."""
        # Implement tokenization logic here
        tokens = []
        # ...
        return tokens
```

### 2. Create a Parser

Next, create a parser for Abstract Syntax Tree generation:

```python
# aether/parsers/rust_parser.py
from aether.parsers.base import BaseParser

class RustParser(BaseParser):
    """Parser for Rust programming language."""

    @property
    def language(self) -> str:
        return "rust"

    def parse(self, code: str) -> dict:
        """Parse Rust code into an AST."""
        # Implement parsing logic here
        # You might use tree-sitter or another parser
        ast = {}
        # ...
        return ast
```

### 3. Register the New Language

Register your new language components:

```python
# aether/tokenizers/__init__.py
from aether.tokenizers.rust_tokenizer import RustTokenizer

TOKENIZERS = {
    # ... existing tokenizers
    "rust": RustTokenizer,
}

# aether/parsers/__init__.py
from aether.parsers.rust_parser import RustParser

PARSERS = {
    # ... existing parsers
    "rust": RustParser,
}
```

### 4. Add Tree-sitter Grammar (Optional)

If you're using tree-sitter for parsing:

1. Add the grammar to your project:

```bash
git submodule add https://github.com/tree-sitter/tree-sitter-rust.git aether/parsers/grammars/tree-sitter-rust
```

2. Build the grammar:

```python
# aether/parsers/setup_grammars.py
# Add to the existing logic:
Language.build_library(
    # ... existing languages
    'aether/parsers/grammars/rust.so',
    ['aether/parsers/grammars/tree-sitter-rust']
)
```

## Creating a Custom Similarity Metric

### 1. Define a New Metric

Create a custom similarity metric:

```python
# aether/metrics/weighted_cosine.py
from aether.metrics.base import BaseMetric
import numpy as np

class WeightedCosineMetric(BaseMetric):
    """Weighted cosine similarity metric."""

    def __init__(self, weights: dict = None):
        self.weights = weights or {
            "tokens": 0.7,
            "structure": 0.3
        }

    @property
    def name(self) -> str:
        return "weighted_cosine"

    def calculate(self, vec1: np.ndarray, vec2: np.ndarray) -> float:
        """Calculate weighted cosine similarity."""
        # Implement weighted similarity logic here
        # ...
        return similarity_score
```

### 2. Register the Metric

Register your custom metric:

```python
# aether/metrics/__init__.py
from aether.metrics.weighted_cosine import WeightedCosineMetric

METRICS = {
    # ... existing metrics
    "weighted_cosine": WeightedCosineMetric,
}
```

## Creating a Custom Output Format

### 1. Define a New Visualizer

Create a custom output format:

```python
# aether/visualization/markdown_report.py
from aether.visualization.base import BaseVisualizer

class MarkdownVisualizer(BaseVisualizer):
    """Markdown report generator."""

    @property
    def format(self) -> str:
        return "markdown"

    @property
    def file_extension(self) -> str:
        return ".md"

    def generate(self, results: dict) -> str:
        """Generate a markdown report."""
        md_content = "# Similarity Analysis Results\n\n"
        # ... build the markdown report
        return md_content
```

### 2. Register the Visualizer

Register your custom visualizer:

```python
# aether/visualization/__init__.py
from aether.visualization.markdown_report import MarkdownVisualizer

VISUALIZERS = {
    # ... existing visualizers
    "markdown": MarkdownVisualizer,
}
```

## Implementing a Custom Detection Algorithm

### 1. Create a Detector

Implement a custom detection algorithm:

```python
# aether/core/ngram_detector.py
from aether.core.detector import BaseDetector

class NGramDetector(BaseDetector):
    """N-gram based similarity detector."""

    def __init__(self, n: int = 3):
        self.n = n

    @property
    def name(self) -> str:
        return f"ngram_{self.n}"

    def extract_features(self, code: str) -> dict:
        """Extract n-gram features from code."""
        # Implement n-gram extraction
        # ...
        return features

    def compare(self, source_features: dict, target_features: dict) -> float:
        """Compare n-gram features."""
        # Implement comparison logic
        # ...
        return similarity_score
```

### 2. Register the Detector

Register your custom detector:

```python
# aether/core/__init__.py
from aether.core.ngram_detector import NGramDetector

DETECTORS = {
    # ... existing detectors
    "ngram": NGramDetector,
}
```

## Adding a Custom Machine Learning Model

### 1. Implement the Model

Create a custom ML model:

```python
# aether/models/transformer_encoder.py
from aether.models.base import BaseModel
import torch.nn as nn

class TransformerEncoder(BaseModel):
    """Transformer-based code embedding model."""

    def __init__(self, config: dict = None):
        self.config = config or {}
        # Initialize the model
        # ...

    @property
    def name(self) -> str:
        return "transformer_encoder"

    def encode(self, code: str) -> list[float]:
        """Encode code into an embedding vector."""
        # Implement encoding logic
        # ...
        return embedding

    def train(self, dataset: list[tuple[str, str, float]]) -> None:
        """Train the model on labeled data."""
        # Implement training logic
        # ...
```

### 2. Register the Model

Register your custom model:

```python
# aether/models/__init__.py
from aether.models.transformer_encoder import TransformerEncoder

MODELS = {
    # ... existing models
    "transformer_encoder": TransformerEncoder,
}
```

## Extending the CLI

### 1. Add a New Command

Create a new CLI command:

```python
# aether/cli/commands/benchmark.py
import click
from aether.cli.utils import common_options

@click.command()
@common_options
@click.option('--dataset', required=True, help='Benchmark dataset path')
@click.option('--iterations', default=5, help='Number of iterations')
def benchmark(dataset, iterations, **kwargs):
    """Benchmark different detection methods."""
    click.echo(f"Running benchmark on {dataset} with {iterations} iterations...")
    # Implement benchmarking logic
    # ...
```

### 2. Register the Command

Register your command with the CLI:

```python
# aether/cli/__init__.py
from aether.cli.commands.benchmark import benchmark

# Add to the existing cli.add_command calls
cli.add_command(benchmark)
```

## Creating Plugins

For more complex extensions, you can create a plugin system:

### 1. Define a Plugin Interface

```python
# aether/plugins/base.py
from abc import ABC, abstractmethod

class AetherPlugin(ABC):
    """Base class for Æther plugins."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Plugin name."""
        pass

    @abstractmethod
    def initialize(self, context: dict) -> None:
        """Initialize the plugin."""
        pass

    @abstractmethod
    def execute(self, *args, **kwargs) -> any:
        """Execute the plugin."""
        pass
```

### 2. Implement a Plugin Manager

```python
# aether/plugins/manager.py
import importlib
import pkgutil
from aether.plugins.base import AetherPlugin

class PluginManager:
    """Manager for Æther plugins."""

    def __init__(self):
        self.plugins = {}

    def discover(self, namespace: str = "aether_plugins") -> None:
        """Discover plugins in the given namespace."""
        # Discover and load plugins
        # ...

    def register(self, plugin: AetherPlugin) -> None:
        """Register a plugin."""
        self.plugins[plugin.name] = plugin

    def get(self, name: str) -> AetherPlugin:
        """Get a plugin by name."""
        return self.plugins.get(name)

    def execute(self, name: str, *args, **kwargs) -> any:
        """Execute a plugin."""
        plugin = self.get(name)
        if plugin:
            return plugin.execute(*args, **kwargs)
        return None
```

## Best Practices for Extension

When extending Æther, follow these best practices:

1. **Use Base Classes**: Always extend the appropriate base classes to ensure compatibility.
2. **Write Tests**: Create tests for your extensions to verify they work correctly.
3. **Document Your Code**: Add docstrings and comments to make your extensions understandable.
4. **Keep Extensions Modular**: Each extension should have a single responsibility.
5. **Follow the Existing Patterns**: Maintain consistency with the existing codebase.

## Next Steps

After extending Æther with your custom components:

- Run tests to ensure everything works correctly: `pytest tests/`
- Update documentation to include your extensions
- Consider contributing back to the main project if your extensions would be broadly useful

For more information, see the [API Documentation](../api/core.md) for detailed interfaces and structures.
