"""
Command-line interfacer for Æther.

This module provides the main entry point for the command-line
interface for Æther, allowing users to perform code similarity
detection from the terminal.
"""

import os
import sys
from typing import Optional

import click

from aether.__version__ import __version__


@click.group()
@click.version_option(version=__version__, prog_name="Æther")
@click.option(
    "--config",
    "-c",
    type=click.Path(exists=True),
    help="Path to the configuration file.",
)
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
@click.option("--quiet", "-q", is_flag=True, help="Suppress all output except errors")
@click.pass_context()
def main(ctx: click.Context, config: Optional[str], verbose: bool, quiet: bool) -> None:
    """
    Æther - Advanced source code similarity detection system.

    Æther identifies similarities, patterns, and potential copyright infringements
    across codebases with high accuracy and efficiency.
    """

    ctx.ensure_object(dict)

    # Store CLI options in context
    ctx.obj["versbose"] = verbose
    ctx.obj["quiet"] = quiet

    # TODO: implement configuration loading
    if config:
        ctx.obj["config"] = {"path": config}

    else:
        ctx.obj["config"] = {}


@main.command()
@click.argument("file1", type=click.Path(exists=True))
@click.argument("file2", type=click.Path(exists=True), required=False)
@click.option(
    "--source",
    "-s",
    type=click.Path(exists=True),
    help="Path to the source directory to compare.",
)
@click.option(
    "--target",
    "-t",
    type=click.Path(exists=True),
    help="Path to the target directory to compare.",
)
@click.option(
    "--threshold",
    "-th",
    type=float,
    default=0.75,
    help="Similarity threshold for comparison (0.0 to 1.0).",
)
@click.option(
    "--format",
    "-f",
    type=click.Choice(["json", "csv", "html"], case_sensitive=False),
    default="json",
    help="Output format for the comparison results.",
)
@click.option("--output", "-o", type=click.Path(), help="Output file path")
@click.option("--skip-comments", is_flag=True, help="Ignore comments in comparison")
@click.pass_context()
def compare(
    ctx: click.Context,
    file1: Optional[str],
    file2: Optional[str],
    source: Optional[str],
    target: Optional[str],
    threshold: float,
    format: str,
    output: Optional[str],
    skip_comments: bool,
) -> None:
    """
    Compare source code files or directories for similarities.

    FILE1 and FILE2 are paths to individual files to compare. Alternatively,
    use --source and --target to compare directories.
    """

    verbose = ctx.obj.get("verbose", False)
    quiet = ctx.obj.get("quiet", False)

    # Determine if comparison mode (files or directories)
    if source or target:
        source_path = source or file1
        target_path = target or file2 or source_path

        if not source_path:
            click.echo("Error: No source path provided", err=True)
            sys.exit(1)

        if not quiet:
            click.echo(f"Comparing code between:")
            click.echo(f"  Source: {source_path}")
            click.echo(f"  Target: {target_path}")
            click.echo(f"  Threshold: {threshold}")

        # TODO: Implement directory comparison logic
        click.echo("Directory comparison is not yet implemented.")

    else:
        if not file1 or not file2:
            click.echo("Error: Two files are required for comparison", err=True)
            sys.exit(1)

        if not quiet:
            click.echo(f"Comparing files:")
            click.echo(f"  File 1: {file1}")
            click.echo(f"  File 2: {file2}")
            click.echo(f"  Threshold: {threshold}")

        # TODO: Implement file comparison logic
        click.echo("File comparison is not yet implemented.")

    # Print settings for debugging
    if verbose:
        click.echo("Settings:")
        click.echo(f"  Threshold: {threshold}")
        click.echo(f"  Output Format: {format}")
        click.echo(f"  Skip Comments: {skip_comments}")

        if output:
            click.echo(f"  Output Path: {output}")


if __name__ == "__main__":
    main(obj={})
