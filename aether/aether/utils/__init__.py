"""
Utility functions and helpers for the Æther project
"""

from aether.utils.file_utils import (
    find_files,
    read_file,
    write_file,
    get_file_extension,
    is_binary_file,
    detect_file_language,
)
from aether.utils.config import (
    load_config,
    save_config,
    merge_configs,
    get_config_path,
)
from aether.utils.logging import (
    setup_logger,
    get_logger,
)

__all__ = [
    # File utilities
    "find_files",
    "read_file",
    "write_file",
    "get_file_extension",
    "is_binary_file",
    "detect_file_language",
    # Configuration utilities
    "load_config",
    "save_config",
    "merge_configs",
    "get_config_path",
    # Logging utilities
    "setup_logger",
    "get_logger",
]
