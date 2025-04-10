"""Utility functions and helpers for the Æther project."""

# File utilities
from aether.utils.file_utils import (
    find_files,
    read_file,
    write_file,
    get_file_extension,
    is_binary_file,
    detect_file_language,
)

# Configuration utilities
from aether.utils.config import (
    load_config,
    save_config,
    merge_configs,
    get_config_path,
    get_default_config,
    find_project_config,
)

# Logging utilities
from aether.utils.logging import (
    setup_logger,
    get_logger,
)

# Text processing utilities
from aether.utils.text_utils import (
    normalize_whitespace,
    remove_comments,
    extract_identifiers,
    normalize_identifiers,
    get_language_keywords,
    tokenize_code,
)

# Profiling utilities
from aether.utils.profiling import (
    timeit,
    memory_usage,
    track_performance,
    Timer,
    MemoryTracker,
    PerformanceStats,
    performance_stats,
)

# Hashing utilities
from aether.utils.hash_utils import (
    md5_hash,
    sha1_hash,
    sha256_hash,
    adler32_hash,
    rolling_hash,
    winnowing_fingerprint,
    simhash,
    hamming_distance,
    jaccard_similarity,
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
