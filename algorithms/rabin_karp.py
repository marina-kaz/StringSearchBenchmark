"""
Rabin-Karp substring search algorithm

Uses hashing to efficiently find a substring in a text.
This algorithm minimizes unnecessary character comparisons 
by leveraging hash values for quicker identification of potential matches.

Time complexity: 
    expected: O(m + n)
    worst: O(m * n)
"""
from typing import Optional


BASE = 31
Q = 2147483647


def gorner_scheme(string: str) -> float:
    """
    Evaluates polynomial using Horner's method,
    which minimizes the number of multiplications.

    Args:
        string (str): text for which to evaluate polynomial

    Returns:
        float: polynomial estimation
    """
    result = ord(string[0])
    for i in range(len(string) - 1):
        result = result * BASE + ord(string[i + 1])
    return result


def calculate_hash(string: str) -> float:
    """
    Calculates polynomial hash for string using Gorner scheme.

    Args:
        string (str): text for which to calculate hash

    Returns:
        float: hash value
    """
    return gorner_scheme(string) % Q


def rabin_karp_search(string: str, substring: str) -> Optional[str]:
    """
    Rabin-Karp substring search algorithm

    Args:
        string (str): text in which to find a substring
        substring (str): substring to find in text

    Returns:
        Optional[int]: position at which substring matching pattern begins
                       if there is one, otherwise None

    Steps:
        1. Compute hash values for the substring and overlapping text windows.
        2. Compare hash values, and if they match, perform a character-by-character check.
        3. Move the window one character at a time and repeat.
    """
    if not substring:
        return None

    sub_hash = calculate_hash(substring)
    m = len(substring)
    current_hash = calculate_hash(string[:m])
    i = 0
    while True:
        if sub_hash == current_hash:
            if substring == string[i : i + m]:
                return i
        if i + m >= len(string):
            break
        current_hash = (
            (current_hash - ord(string[i]) * BASE ** (m - 1)) * BASE
            + ord(string[i + m])
        ) % Q
        i += 1
