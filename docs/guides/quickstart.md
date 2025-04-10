# Quickstart Guide

This guide will help you get started with Æther quickly. We'll cover basic usage patterns for detecting code similarities.

## Basic Comparison

The simplest way to use Æther is to compare two source code files:

```bash
aether compare file1.py file2.py
```

This command will:

1. Analyze both files
2. Calculate similarity scores
3. Output a report showing the similarity percentage and highlighted matching sections

## Setting a Threshold

You can set a custom similarity threshold (between 0.0 and 1.0):

```bash
aether compare file1.py file2.py --threshold 0.8
```

Only similarities above the specified threshold will be reported.

## Comparing Directories

To compare entire codebases:

```bash
aether compare --source path/to/original/repo --target path/to/suspected/repo
```

This will recursively analyze all compatible source files in both directories and generate a comprehensive report.

## Output Formats

Æther supports multiple output formats:

```bash
# Generate an HTML report
aether compare file1.py file2.py --format html --output report.html

# Generate JSON output
aether compare file1.py file2.py --format json --output results.json

# Simple text output
aether compare file1.py file2.py --format text
```

## Choosing Detection Methods

You can specify which detection methods to use:

```bash
# Use AST-based comparison
aether compare file1.py file2.py --use-ast

# Use machine learning-based detection
aether compare file1.py file2.py --use-ml

# Skip analyzing comments
aether compare file1.py file2.py --skip-comments

# Combine multiple methods
aether compare file1.py file2.py --use-ast --use-ml --skip-comments
```

## Working with Multiple Languages

Æther automatically detects file languages based on extensions, but you can specify the language explicitly:

```bash
aether compare file1.txt file2.txt --language python
```

## Saving and Viewing Reports

Generate and save an HTML report for easy viewing:

```bash
aether compare --source path/to/original --target path/to/suspected --format html --output similarity_report.html
```

Open the HTML file in any web browser to explore the results interactively.

## Example Workflow

Here's a typical workflow for checking student assignments for plagiarism:

```bash
# Create a directory for results
mkdir -p results

# Compare all student submissions against each other
aether compare --source ./student_submissions --target ./student_submissions --format html --output results/plagiarism_check.html --threshold 0.7 --use-ast --use-ml

# Open the report
open results/plagiarism_check.html
```

## Configuration File

For repeated use with the same settings, create a configuration file:

```toml
# aether.toml
[tool.aether]
threshold = 0.75
ignore_comments = true
use_ast = true
use_ml_model = true
output_format = "html"
```

Then run Æther with:

```bash
aether compare file1.py file2.py --config aether.toml
```

## Next Steps

Now that you understand the basics, check out:

- [Configuration Guide](configuration.md) for detailed configuration options
- [Advanced Features](../examples/advanced_features.md) for more sophisticated usage
- [API Documentation](../api/core.md) if you want to integrate Æther into your own projects
