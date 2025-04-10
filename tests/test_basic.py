"""Basic tests for the Æther package."""

import os
import pytest

from aether.__version__ import __version__
from aether.utils.file_utils import get_file_extension, detect_file_language
from aether.utils.text_utils import normalize_whitespace
from aether.utils.hash_utils import md5_hash


def test_version():
    """Test that the version is defined."""
    assert __version__ is not None
    assert isinstance(__version__, str)


def test_get_file_extension():
    """Test the get_file_extension function."""
    assert get_file_extension("test.py") == ".py"
    assert get_file_extension("path/to/test.py") == ".py"
    assert get_file_extension("path/to/test") == ""
    assert get_file_extension("path.to/test.js") == ".js"


def test_detect_file_language():
    """Test the detect_file_language function."""
    assert detect_file_language("test.py") == "python"
    assert detect_file_language("test.java") == "java"
    assert detect_file_language("test.cpp") == "cpp"
    assert detect_file_language("test.unknown") is None


def test_normalize_whitespace():
    """Test the normalize_whitespace function."""
    # Test tab conversion and trailing whitespace removal
    assert normalize_whitespace("hello\tworld") == "hello    world"
    assert normalize_whitespace("hello  ") == "hello"

    # Test line ending normalization
    assert normalize_whitespace("hello\r\nworld") == "hello\nworld"
    assert normalize_whitespace("hello\rworld") == "hello\nworld"

    # Test mixed whitespace issues
    mixed = "def example():\r\n\t# Comment\r\n\treturn True  "
    expected = "def example():\n    # Comment\n    return True"
    assert normalize_whitespace(mixed) == expected


def test_md5_hash():
    """Test the md5_hash function."""
    assert md5_hash("hello world") == "5eb63bbbe01eeed093cb22bb8f5acdc3"
    assert md5_hash("") == "d41d8cd98f00b204e9800998ecf8427e"

    # Test different inputs produce different hashes
    assert md5_hash("test1") != md5_hash("test2")


def test_import_all_modules():
    """Test that all main modules can be imported."""
    # This is a basic smoke test to ensure modules are properly packaged
    import aether
    import aether.utils

    # These will raise ImportError if modules aren't properly structured
    assert aether is not None
    assert aether.utils is not None
