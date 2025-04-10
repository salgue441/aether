"""Utility functions and helpers for the Æther project."""

# Configuration utilities
from aether.utils.config import (
    find_project_config,
    get_config_path,
    get_default_config,
    load_config,
    merge_configs,
    save_config,
)

# File utilities
from aether.utils.file_utils import (
    detect_file_language,
    find_files,
    get_file_extension,
    is_binary_file,
    read_file,
    write_file,
)

# Hashing utilities
from aether.utils.hash_utils import (
    adler32_hash,
    hamming_distance,
    jaccard_similarity,
    md5_hash,
    rolling_hash,
    sha1_hash,
    sha256_hash,
    simhash,
    winnowing_fingerprint,
)

# Logging utilities
from aether.utils.logging import (
    get_logger,
    setup_logger,
)

# Profiling utilities
from aether.utils.profiling import (
    MemoryTracker,
    PerformanceStats,
    Timer,
    memory_usage,
    performance_stats,
    timeit,
    track_performance,
)

# Text processing utilities
from aether.utils.text_utils import (
    extract_identifiers,
    get_language_keywords,
    normalize_identifiers,
    normalize_whitespace,
    remove_comments,
    tokenize_code,
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
    "get_default_config",
    "find_project_config",
    # Logging utilities
    "setup_logger",
    "get_logger",
    # Text processing utilities
    "normalize_whitespace",
    "remove_comments",
    "extract_identifiers",
    "normalize_identifiers",
    "get_language_keywords",
    "tokenize_code",
    # Profiling utilities
    "timeit",
    "memory_usage",
    "track_performance",
    "Timer",
    "MemoryTracker",
    "PerformanceStats",
    "performance_stats",
    # Hashing utilities
    "md5_hash",
    "sha1_hash",
    "sha256_hash",
    "adler32_hash",
    "rolling_hash",
    "winnowing_fingerprint",
    "simhash",
    "hamming_distance",
    "jaccard_similarity",
]
