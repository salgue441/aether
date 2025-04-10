"""Configuration utilities for the Æther project."""

import os
import pathlib
from typing import Any, Dict, Optional
import tomli
import tomli_w


def get_config_path() -> str:
    """Get the path to the user's config directory.

    Returns:
        Path to the user's config directory.
    """
    if os.name == "nt":  # Windows
        config_dir = os.path.join(os.environ.get("APPDATA", ""), "aether")

    else:  # Unix-like
        config_dir = os.path.join(
            os.environ.get("XDG_CONFIG_HOME", os.path.expanduser("~/.config")),
            "aether",
        )

    os.makedirs(config_dir, exist_ok=True)
    return config_dir


def load_config(config_path: str) -> Dict[str, Any]:
    """
    Load configuration from a TOML file.

    Args:
        config_path: Path to the configuration file.

    Returns:
        The configuration as a dictionary.

    Raises:
        FileNotFoundError: If the config file doesn't exist.
        tomli.TOMLDecodeError: If the TOML file is invalid.
    """
    try:
        with open(config_path, "rb") as file:
            config = tomli.load(file)

        if "tool" in config and "aether" in config["tool"]:
            return config["tool"]["aether"]

        return config
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found: {config_path}")

    except tomli.TOMLDecodeError as e:
        raise tomli.TOMLDecodeError(f"Invalid TOML file: {e}", "", 0)


def save_config(config: Dict[str, Any], config_path: str) -> None:
    """
    Save configuration to a TOML file.

    Args:
        config: The configuration to save.
        config_path: Path to the configuration file.

    Raises:
        IOError: If the file can't be written.
    """

    os.makedirs(os.path.dirname(os.path.abspath(config_path)), exist_ok=True)
    if not any(key in config for key in ["tool", "aether"]):
        config = {"aether": config}

    with open(config_path, "wb") as file:
        tomli_w.dump(config, file)


def merge_configs(
    base_config: Dict[str, Any], override_config: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Merge two configurations, with override_config taking precedence.

    Args:
        base_config: The base configuration.
        override_config: Configuration to override the base configuration.

    Returns:
        The merged configuration.
    """

    merged = base_config.copy()
    for key, value in override_config.items():
        if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
            merged[key] = merge_configs(merged[key], value)
        else:
            merged[key] = value

    return merged


def get_default_config() -> Dict[str, Any]:
    """
    Get the default configuration for Æther.

    Returns:
        The default configuration.
    """

    return {
        "threshold": 0.75,
        "ignore_comments": True,
        "consider_variable_names": False,
        "min_token_length": 3,
        "use_ml_model": False,
        "use_ast": True,
        "normalize_identifiers": True,
        "output_format": "text",
        "include_snippets": True,
        "include_metrics": True,
        "languages": ["python", "java", "cpp"],
    }


def find_project_config() -> Optional[str]:
    """
    Find the project configuration file in the current directory or its parents.

    Returns:
        Path to the configuration file if found, None otherwise.
    """

    config_files = ["aether.toml", "pyproject.toml"]
    current_dir = pathlib.Path.cwd()

    while current_dir != current_dir.parent:
        for config_file in config_files:
            config_path = current_dir / config_file

            if config_path.exists():
                return str(config_path)

        current_dir = current_dir.parent

    return None
