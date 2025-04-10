"""
Hashing utilities for the Æther project.
"""

import hashlib
import zlib
from typing import Any, Callable, List, Tuple, Union

# Type alias for hash function
HashFunction = Callable[[str], str]


def md5_hash(text: str) -> str:
    """
    Compute MD5 hash of text.

    Args:
        text: Input text to hash.

    Returns:
        MD5 hash as a hexadecimal string.
    """

    return hashlib.md5(text.encode()).hexdigest()


def sha1_hash(text: str) -> str:
    """
    Compute SHA1 hash of text.

    Args:
        text: Input text to hash.

    Returns:
        SHA1 hash as a hexadecimal string.
    """

    return hashlib.sha1(text.encode()).hexdigest()


def sha256_hash(text: str) -> str:
    """
    Compute SHA256 hash of text.

    Args:
        text: Input text to hash.

    Returns:
        SHA256 hash as a hexadecimal string.
    """

    return hashlib.sha256(text.encode()).hexdigest()


def adler32_hash(text: str) -> str:
    """
    Compute Adler32 hash of text.

    This is faster than cryptographic hashes and suitable for fingerprinting.

    Args:
        text: Input text to hash.

    Returns:
        Adler32 hash as a hexadecimal string.
    """

    return hex(zlib.adler32(text.encode()))[2:]


def rolling_hash(text: str, base: int = 256, mod: int = 101) -> List[int]:
    """
    Compute a rolling hash for Rabin-Karp algorithm.

    Args:
        text: Input text to hash.
        base: Base for the rolling hash function.
        mod: Modulus for the rolling hash function.

    Returns:
        List of hash values, one for each position.
    """

    n = len(text)
    hash_values = [0] * (n + 1)

    for i in range(n):
        hash_values[i + 1] = (hash_values[i] * base + ord(text[i])) % mod

    return hash_values


def winnowing_fingerprint(text: str, k: int = 5, w: int = 4) -> List[Tuple[int, int]]:
    """
    Compute a winnowing fingerprint for document similarity.

    Implementation of the winnowing algorithm described in the paper:
    "Winnowing: Local Algorithms for Document Fingerprinting"

    Args:
        text: Input text to fingerprint.
        k: Size of k-grams.
        w: Window size for winnowing.

    Returns:
        List of (position, hash) tuples representing the fingerprint.
    """

    if len(text) < k:
        return []

    kgrams = [text[i : i + k] for i in range(len(text) - k + 1)]
    hashes = [zlib.adler32(kgram.encode()) for kgram in kgrams]
    fingerprints = []

    for i in range(len(hashes) - w + 1):
        window = hashes[i : i + w]

        min_hash = min(window)
        min_pos = i + window.index(min_hash)

        if not fingerprints or fingerprints[-1][0] != min_pos:
            fingerprints.append((min_pos, min_hash))

    return fingerprints


def simhash(text: str, num_bits: int = 64) -> int:
    """
    Compute SimHash of text for similarity detection.

    SimHash is a technique for quickly estimating how similar documents are.

    Args:
        text: Input text to hash.
        num_bits: Number of bits in the resulting hash.

    Returns:
        SimHash value as an integer.
    """

    v = [0] * num_bits
    tokens = text.split()

    for token in tokens:
        token_hash = int(sha256_hash(token), 16)

        for i in range(num_bits):
            bit = (token_hash >> i) & 1
            v[i] += 1 if bit else -1

    simhash = 0
    for i in range(num_bits):
        if v[i] > 0:
            simhash |= 1 << i

    return simhash


def hamming_distance(hash1: int, hash2: int) -> int:
    """
    Compute Hamming distance between two hashes.

    Args:
        hash1: First hash value.
        hash2: Second hash value.

    Returns:
        Number of bit positions in which the hashes differ.
    """

    xor = hash1 ^ hash2
    count = 0

    while xor:
        count += xor & 1
        xor >>= 1

    return count


def jaccard_similarity(
    set1: Union[List[Any], set], set2: Union[List[Any], set]
) -> float:
    """
    Compute Jaccard similarity between two sets.

    Args:
        set1: First set of elements.
        set2: Second set of elements.

    Returns:
        Jaccard similarity coefficient (0.0 to 1.0).
    """

    s1 = set(set1) if not isinstance(set1, set) else set1
    s2 = set(set2) if not isinstance(set2, set) else set2

    intersection = len(s1 & s2)
    union = len(s1 | s2)

    if union == 0:
        return 1.0

    return intersection / union
