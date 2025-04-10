"""
File utility functions for the Æther project
"""

import fnmatch
import os
import pathlib
from typing import List, Optional, Set, Tuple


def find_files(
    directory: str,
    include_patterns: List[str] = None,
    exclude_patterns: List[str] = None,
    recursive: bool = False,
) -> List[str]:
    """
    Find files in a directory that match the given patterns.

    Args:
        directory (str): The directory to search in.
        include_patterns (List[str]): A list of glob patterns to include.
        exclude_patterns (List[str]): A list of glob patterns to exclude.
        recursive (bool): Whether to search recursively.

    Returns:
      A list of file paths that match the criteria
    """

    include_patterns = include_patterns or ["*"]
    exclude_patterns = exclude_patterns or []
    matching_files = []

    if recursive:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)

                included = any(
                    fnmatch.fnmatch(file, pattern) for pattern in include_patterns
                )

                excluded = any(
                    fnmatch.fnmatch(file, pattern) for pattern in exclude_patterns
                )

                if included and not excluded:
                    matching_files.append(file_path)

    else:
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)

            if os.path.isfile(file_path):
                included = any(
                    fnmatch.fnmatch(file, pattern) for pattern in include_patterns
                )

                excluded = any(
                    fnmatch.fnmatch(file, pattern) for pattern in exclude_patterns
                )

                if included and not excluded:
                    matching_files.append(file_path)

    return matching_files


def read_file(file_path: str, encoding: str = "utf-8") -> str:
    """
    Read text from a file.

    Args:
      file_path: The path to the file.
      encoding: The encoding to use for reading the file.

    Returns:
      The content of the file as a string.

    Raises:
      FileNotFoundError: If the file doesn't exist.
      UnicodeDecodeError: If the file can't be decoded with the given encoding.
    """

    with open(file_path, "r", encoding=encoding) as file:
        return file.read()


def write_file(file_path: str, content: str, encoding: str = "utf-8") -> None:
    """
    Write text to a file.

    Args:
        file_path: Path to the file to write.
        content: The content to write to the file.
        encoding: File encoding.

    Raises:
        IOError: If the file can't be written.
    """
    os.makedirs(os.path.dirname(os.path.abspath(file_path)), exist_ok=True)

    with open(file_path, "w", encoding=encoding) as file:
        file.write(content)


def get_file_extension(file_path: str) -> str:
    """
    Get the extension of a file.

    Args:
      file_path: The path to the file.

    Returns:
      The file extension, including the dot (e.g., '.txt').
    """

    return os.path.splitext(file_path)[1].lower()


def is_binary_file(file_path: str) -> bool:
    """
    Check if a file is binary.

    Args:
        file_path: The path to the file.

    Returns:
        True if the file is binary, False otherwise.

    Raises:
        FileNotFoundError: If the file doesn't exist.
    """

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            file.read(1024)

        return False

    except UnicodeDecodeError:
        return True


def detect_file_language(file_path: str) -> Optional[str]:
    """
    Detect the programming language of a file based on its extension

    Args:
      file_path: Path to the file

    Returns:
      The detected language or None if the language is not recognized
    """

    extension_map = {
        ".py": "python",
        ".java": "java",
        ".cpp": "cpp",
        ".cc": "cpp",
        ".c": "c",
        ".h": "c",
        ".hpp": "cpp",
        ".js": "javascript",
        ".ts": "typescript",
        ".rb": "ruby",
        ".go": "go",
        ".php": "php",
        ".cs": "csharp",
        ".swift": "swift",
        ".kt": "kotlin",
        ".rs": "rust",
    }

    ext = get_file_extension(file_path)
    return extension_map.get(ext)
