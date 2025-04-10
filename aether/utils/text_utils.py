"""
Text processing utilities for the Æther project
"""

import re
from typing import List


def normalize_whitespace(text: str) -> str:
    """Normalize whitespace in text.

    Args:
        text: The input text.

    Returns:
        Text with consistent whitespace:
        - Convert tabs to spaces
        - Trim trailing whitespace
        - Ensure single newlines
    """

    text = text.replace("\t", "    ")
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    lines = [line.rstrip() for line in text.split("\n")]
    return "\n".join(lines)


def remove_comments(code: str, language: str) -> str:
    """
    Remove comments from code

    Args:
      code (str): The code to process.
      language (str): The programming language of the code.
        Supported languages are 'python', 'cpp', and 'java'.

    Returns:
      str: The code without comments.
    """

    patterns = {
        "python": [
            (r"#.*?$", ""),  # Single-line comments
            (r'""".*?"""', "", re.DOTALL),  # Multi-line docstrings
            (r"'''.*?'''", "", re.DOTALL),  # Multi-line docstrings
        ],
        "java": [
            (r"//.*?$", ""),  # Single-line comments
            (r"/\*.*?\*/", "", re.DOTALL),  # Multi-line comments
        ],
        "cpp": [
            (r"//.*?$", ""),  # Single-line comments
            (r"/\*.*?\*/", "", re.DOTALL),  # Multi-line comments
        ],
    }

    patterns_to_use = patterns.get(language.lower(), patterns["cpp"])
    result = code

    for pattern, replacement, *flags in patterns_to_use:
        flag = flags[0] if flags else 0
        result = re.sub(pattern, replacement, result, flags=flag)

    return result


def extract_identifiers(code: str, language: str) -> List[str]:
    """
    Extract identifiers (variable names, function names, etc.) from code.

    Args:
      code (str): The code to process.
      language (str): The programming language of the code.
        Supported languages are 'python', 'cpp', and 'java'.

    Returns:
      List[str]: A list of identifiers found in the code.
    """

    patterns = {
        "python": r"[a-zA-Z_][a-zA-Z0-9_]*",
        "java": r"[a-zA-Z_$][a-zA-Z0-9_$]*",
        "cpp": r"[a-zA-Z_][a-zA-Z0-9_]*",
    }

    pattern = patterns.get(language.lower(), r"[a-zA-Z_][a-zA-Z0-9_]*")
    identifiers = re.findall(pattern, code)
    keywords = get_language_keywords(language)

    return [ident for ident in identifiers if ident not in keywords]


def normalize_identifiers(code: str, language: str) -> str:
    """
    Replace all identifiers with generic placeholders

    Args:
      code (str): The code to process.
      language (str): The programming language of the code.
        Supported languages are 'python', 'cpp', and 'java'.

    Returns:
      str: The code with identifiers replaced by generic placeholders.
    """

    identifiers = extract_identifiers(code, language)
    unique_identifiers = sorted(set(identifiers))

    mapping = {ident: f"VAR_{i}" for i, ident in enumerate(unique_identifiers)}
    result = code

    for ident, placeholder in mapping.items():
        pattern = r"\b" + re.escape(ident) + r"\b"
        result = re.sub(pattern, placeholder, result)

    return result


def get_language_keywords(language: str) -> List[str]:
    """
    Get keywords for a specific programming language

    Args:
      language (str): The programming language to get keywords for.
        Supported languages are 'python', 'cpp', and 'java'.

    Returns:
      List[str]: A list of keywords for the specified programming language.
    """

    keywords = {
        "python": [
            "False",
            "None",
            "True",
            "and",
            "as",
            "assert",
            "async",
            "await",
            "break",
            "class",
            "continue",
            "def",
            "del",
            "elif",
            "else",
            "except",
            "finally",
            "for",
            "from",
            "global",
            "if",
            "import",
            "in",
            "is",
            "lambda",
            "nonlocal",
            "not",
            "or",
            "pass",
            "raise",
            "return",
            "try",
            "while",
            "with",
            "yield",
        ],
        "java": [
            "abstract",
            "assert",
            "boolean",
            "break",
            "byte",
            "case",
            "catch",
            "char",
            "class",
            "const",
            "continue",
            "default",
            "do",
            "double",
            "else",
            "enum",
            "extends",
            "final",
            "finally",
            "float",
            "for",
            "goto",
            "if",
            "implements",
            "import",
            "instanceof",
            "int",
            "interface",
            "long",
            "native",
            "new",
            "package",
            "private",
            "protected",
            "public",
            "return",
            "short",
            "static",
            "strictfp",
            "super",
            "switch",
            "synchronized",
            "this",
            "throw",
            "throws",
            "transient",
            "try",
            "void",
            "volatile",
            "while",
        ],
        "cpp": [
            "alignas",
            "alignof",
            "and",
            "and_eq",
            "asm",
            "auto",
            "bitand",
            "bitor",
            "bool",
            "break",
            "case",
            "catch",
            "char",
            "char8_t",
            "char16_t",
            "char32_t",
            "class",
            "compl",
            "concept",
            "const",
            "consteval",
            "constexpr",
            "constinit",
            "const_cast",
            "continue",
            "co_await",
            "co_return",
            "co_yield",
            "decltype",
            "default",
            "delete",
            "do",
            "double",
            "dynamic_cast",
            "else",
            "enum",
            "explicit",
            "export",
            "extern",
            "false",
            "float",
            "for",
            "friend",
            "goto",
            "if",
            "inline",
            "int",
            "long",
            "mutable",
            "namespace",
            "new",
            "noexcept",
            "not",
            "not_eq",
            "nullptr",
            "operator",
            "or",
            "or_eq",
            "private",
            "protected",
            "public",
            "register",
            "reinterpret_cast",
            "requires",
            "return",
            "short",
            "signed",
            "sizeof",
            "static",
            "static_assert",
            "static_cast",
            "struct",
            "switch",
            "template",
            "this",
            "thread_local",
            "throw",
            "true",
            "try",
            "typedef",
            "typeid",
            "typename",
            "union",
            "unsigned",
            "using",
            "virtual",
            "void",
            "volatile",
            "wchar_t",
            "while",
            "xor",
            "xor_eq",
        ],
    }

    return keywords.get(language.lower(), [])


def tokenize_code(code: str) -> List[str]:
    """
    Split code into tokens.

    This is a simple tokenizer that splits on whitespace and punctuation.
    For more advanced tokenization, language-specific tokenizers
    should be used.

    Args:
        code (str): The code to tokenize.

    Returns:
        List[str]: A list of tokens.
    """

    pattern = r'([a-zA-Z_][a-zA-Z0-9_]*|"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'|\d+|\S)'
    tokens = re.findall(pattern, code)

    return [token for token in tokens if token.strip()]
