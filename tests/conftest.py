"""
Test configuration and fixtures for Æther tests.
"""

import os
import tempfile
from typing import Generator, Tuple

import pytest


@pytest.fixture
def temp_file() -> Generator[str, None, None]:
    """
    Create a temporary file for testing.

    Yields:
        Path to a temporary file that will be deleted after the test.
    """

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name

    yield tmp_path
    if os.path.exists(tmp_path):
        os.unlink(tmp_path)


@pytest.fixture
def sample_code_files() -> Generator[Tuple[str, str], None, None]:
    """
    Create temporary files with sample code for testing.

    Yields:
        Tuple of (file1_path, file2_path) containing sample code files.
    """

    code1 = """
def factorial(n):
    # Calculate factorial
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def main():
    print(factorial(5))
    """

    code2 = """
def factorial(num):
    # Compute factorial
    if num <= 1:
        return 1
    return num * factorial(num - 1)

def main():
    print(factorial(5))
    """

    with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as tmp1:
        tmp1.write(code1.encode("utf-8"))
        file1_path = tmp1.name

    with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as tmp2:
        tmp2.write(code2.encode("utf-8"))
        file2_path = tmp2.name

    yield (file1_path, file2_path)

    if os.path.exists(file1_path):
        os.unlink(file1_path)

    if os.path.exists(file2_path):
        os.unlink(file2_path)


@pytest.fixture
def sample_directory() -> Generator[str, None, None]:
    """Create a temporary directory with sample files for testing.

    Yields:
        Path to a temporary directory that will be deleted after the test.
    """
    temp_dir = tempfile.mkdtemp()

    # Create a few files in the directory
    files = {
        "test1.py": 'def hello(): return "world"',
        "test2.py": 'def goodbye(): return "farewell"',
        "README.md": "# Test Directory",
        "subfolder/test3.py": "def nested(): pass",
    }

    for file_path, content in files.items():
        full_path = os.path.join(temp_dir, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w") as f:
            f.write(content)

    yield temp_dir

    import shutil

    shutil.rmtree(temp_dir)
