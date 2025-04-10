import os
import tempfile
from typing import Generator

import pytest

from aether.utils.file_utils import (
    detect_file_language,
    find_files,
    get_file_extension,
    is_binary_file,
    read_file,
    write_file,
)


@pytest.fixture
def sample_directory() -> Generator[str, None, None]:
    """Create a temporary directory with sample files for testing."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some sample files
        write_file(os.path.join(temp_dir, "file1.py"), "print('Hello, world!')")
        write_file(os.path.join(temp_dir, "file2.py"), "x = 10")
        write_file(os.path.join(temp_dir, "file3.txt"), "Plain text file")

        # Create a subdirectory
        subdir = os.path.join(temp_dir, "subdir")
        os.makedirs(subdir, exist_ok=True)

        # Add files to the subdirectory
        write_file(os.path.join(subdir, "file4.py"), "def test(): pass")
        write_file(os.path.join(subdir, "file5.java"), "public class Test {}")

        yield temp_dir


def test_find_files(sample_directory: str) -> None:
    """Test finding files with specific patterns."""
    # Find all files
    all_files = find_files(sample_directory)
    assert len(all_files) == 5

    # Find only Python files
    py_files = find_files(sample_directory, include_patterns=["*.py"])
    assert len(py_files) == 3

    # Find files with exclusion
    non_py_files = find_files(
        sample_directory, include_patterns=["*"], exclude_patterns=["*.py"]
    )
    assert len(non_py_files) == 2

    # Non-recursive search
    top_level_files = find_files(sample_directory, recursive=False)
    assert len(top_level_files) == 3


def test_read_write_file(sample_directory: str) -> None:
    """Test reading and writing files."""
    test_file = os.path.join(sample_directory, "test_read_write.txt")
    test_content = "Test content for read/write operations."

    # Write to the file
    write_file(test_file, test_content)

    # Read from the file
    read_content = read_file(test_file)

    assert read_content == test_content


def test_get_file_extension() -> None:
    """Test getting file extensions."""
    assert get_file_extension("file.txt") == ".txt"
    assert get_file_extension("file.tar.gz") == ".gz"
    assert get_file_extension("file") == ""
    assert get_file_extension("/path/to/file.py") == ".py"


def test_is_binary_file(sample_directory: str) -> None:
    """Test binary file detection."""
    text_file = os.path.join(sample_directory, "text_file.txt")
    write_file(text_file, "This is a text file.")

    assert not is_binary_file(text_file)

    # Create a simple binary file
    binary_file = os.path.join(sample_directory, "binary_file.bin")
    with open(binary_file, "wb") as f:
        f.write(b"\x00\x01\x02\x03")

    assert is_binary_file(binary_file)


def test_detect_file_language() -> None:
    """Test detecting file language based on extension."""
    assert detect_file_language("file.py") == "python"
    assert detect_file_language("file.java") == "java"
    assert detect_file_language("file.cpp") == "cpp"
    assert detect_file_language("file.txt") is None
    assert detect_file_language("file.unknown") is None


def test_write_file_creates_directories(tmpdir):
    """Test that write_file creates directories if they don't exist."""
    # Create a nested path that doesn't exist yet
    deep_file = os.path.join(tmpdir, "a/b/c/test.txt")

    # Write to the file
    write_file(deep_file, "test content")

    # Check that the file exists and has the right content
    assert os.path.exists(deep_file)
    with open(deep_file, "r") as f:
        assert f.read() == "test content"
