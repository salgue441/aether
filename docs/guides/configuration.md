# Configuration Guide

Æther offers extensive configuration options to fine-tune its behavior. This guide covers all the available configuration options and how to use them.

## Configuration Methods

You can configure Æther in three ways:

1. **Command-line arguments**: For one-time settings
2. **Configuration files**: For persistent settings
3. **Environment variables**: For system-wide settings

## Configuration File Formats

Æther supports configuration via:

### pyproject.toml

You can add Æther configuration to your project's `pyproject.toml`:

```toml
[tool.aether]
# Detection settings
threshold = 0.75
ignore_comments = true
consider_variable_names = false
min_token_length = 3

# Machine learning model settings
use_ml_model = true
model_path = "models/similarity_model.pkl"
embedding_dim = 128

# AST analysis settings
use_ast = true
normalize_identifiers = true
consider_structure_only = false

# Output settings
output_format = "html"
include_snippets = true
include_metrics = true

# Languages to support
languages = [
    "python",
    "java",
    "cpp",
]
```

### Dedicated Configuration File

You can also use a dedicated `aether.toml` file:

```toml
[detection]
threshold = 0.75
ignore_comments = true
consider_variable_names = false
min_token_length = 3

[ml]
use_ml_model = true
model_path = "models/similarity_model.pkl"
embedding_dim = 128

[ast]
use_ast = true
normalize_identifiers = true
consider_structure_only = false

[output]
format = "html"
include_snippets = true
include_metrics = true

[languages]
supported = ["python", "java", "cpp"]
```

## Configuration Options

### Detection Settings

| Option                    | Description                          | Default | CLI Flag               |
| ------------------------- | ------------------------------------ | ------- | ---------------------- |
| `threshold`               | Similarity threshold (0.0-1.0)       | 0.75    | `--threshold`          |
| `ignore_comments`         | Exclude comments from analysis       | true    | `--skip-comments`      |
| `consider_variable_names` | Include variable names in comparison | false   | `--consider-variables` |
| `min_token_length`        | Minimum token length to consider     | 3       | `--min-token-length`   |

### Machine Learning Settings

| Option          | Description                  | Default                       | CLI Flag          |
| --------------- | ---------------------------- | ----------------------------- | ----------------- |
| `use_ml_model`  | Use ML-based detection       | true                          | `--use-ml`        |
| `model_path`    | Path to pre-trained model    | "models/similarity_model.pkl" | `--model-path`    |
| `embedding_dim` | Dimension of code embeddings | 128                           | `--embedding-dim` |

### AST Analysis Settings

| Option                    | Description                              | Default | CLI Flag           |
| ------------------------- | ---------------------------------------- | ------- | ------------------ |
| `use_ast`                 | Use AST-based detection                  | true    | `--use-ast`        |
| `normalize_identifiers`   | Replace variable names with placeholders | true    | `--normalize-ids`  |
| `consider_structure_only` | Only consider code structure             | false   | `--structure-only` |

### Output Settings

| Option             | Description                           | Default | CLI Flag             |
| ------------------ | ------------------------------------- | ------- | -------------------- |
| `output_format`    | Format for results (text, json, html) | "text"  | `--format`           |
| `include_snippets` | Include matching code snippets        | true    | `--include-snippets` |
| `include_metrics`  | Include detailed metrics              | true    | `--include-metrics`  |

### Language Settings

| Option      | Description          | Default                   | CLI Flag      |
| ----------- | -------------------- | ------------------------- | ------------- |
| `languages` | Languages to support | ["python", "java", "cpp"] | `--languages` |

## Environment Variables

You can override settings with environment variables:

```bash
# Set similarity threshold
export AETHER_THRESHOLD=0.8

# Enable/disable features
export AETHER_USE_AST=1
export AETHER_USE_ML=0

# Set output format
export AETHER_OUTPUT_FORMAT=json
```

## Command-line Arguments

All configuration options can be set via command-line arguments:

```bash
aether compare \
  --source src/ \
  --target target/ \
  --threshold 0.8 \
  --use-ast \
  --use-ml \
  --format html \
  --output report.html \
  --skip-comments \
  --normalize-ids
```

## Configuration Precedence

Æther uses the following precedence order (highest to lowest):

1. Command-line arguments
2. Environment variables
3. Project-specific configuration file (`./aether.toml`)
4. User configuration file (`~/.config/aether/config.toml`)
5. System-wide configuration file (`/etc/aether/config.toml`)
6. Default values

## Advanced Configuration

### Customizing ML Models

To use a custom ML model:

```toml
[tool.aether.ml]
model_path = "path/to/custom/model.pkl"
tokenizer_path = "path/to/custom/tokenizer.json"
custom_model_type = "transformer"  # or "embedding"
```

### Fine-tuning AST Analysis

For detailed AST analysis configuration:

```toml
[tool.aether.ast]
use_ast = true
normalize_identifiers = true
ignore_literal_values = true
node_types_to_ignore = ["comment", "string_literal", "numeric_literal"]
max_tree_depth = 10
max_children_per_node = 100
```

### Output Customization

To customize the HTML report:

```toml
[tool.aether.output.html]
template_path = "path/to/custom/template.html"
highlight_style = "github"  # or "monokai", "vs", etc.
include_line_numbers = true
collapse_similar_sections = true
```

## Example Configurations

### Academic Setting

```toml
[tool.aether]
threshold = 0.6  # Lower threshold to catch more potential matches
ignore_comments = true
normalize_identifiers = true
output_format = "html"
include_metrics = true
```

### Copyright Compliance

```toml
[tool.aether]
threshold = 0.8  # Higher threshold for stronger evidence
use_ast = true
use_ml_model = true
min_token_length = 5
output_format = "json"
```

### Code Quality Analysis

```toml
[tool.aether]
threshold = 0.9  # Very high threshold for near-identical code
ignore_comments = true
consider_variable_names = true
output_format = "html"
```

## Next Steps

Now that you understand how to configure Æther, check out:

- [Extending Æther](extending.md) to learn how to customize and extend functionality
- [Advanced Features](../examples/advanced_features.md) for more sophisticated use cases
