"""
The Knuth-Morris-Pratt substring search algorithm 

This algorithm avoids redundant comparisons
by using prefix function.

Time complexity: O(n + m)
"""
from typing import Optional


def get_pi(substring: str) -> list[int]:
    """
    Calculates prefix function.

    Args:
        string (str): text for which to calculate prefix function

    Returns:
        list[int]: prefix function value
    """
    pi = [0] * len(substring)
    j, i = 0, 1

    while i < len(substring):
        if substring[i] == substring[j]:
            pi[i] = j + 1
            j += 1
            i += 1
        else:
            if j == 0:
                pi[i] = 0
                i += 1
            else:
                j = pi[j - 1]
    return pi


def knuth_morris_pratt_search(string: str, substring: str) -> Optional[str]:
    """
    Knuth-Morris-Pratt substring search algorithm

    Args:
        string (str): text in which to find a substring
        substring (str): substring to find in text

    Returns:
        Optional[int]: position at which substring matching pattern begins
                       if there is one, otherwise None

    Steps:
        1. Build a prefix function to determine the longest proper prefix
           that is also a suffix for each substring.
        2. Use the prefix function to skip unnecessary comparisons
           during the search.
        3. Iterate through the text and substring concurrently, adjusting
           the position based on the prefix function.
    """
    if not substring:
        return None

    pi = get_pi(substring)
    m = len(substring)
    n = len(string)

    i, j = 0, 0
    while i < n:
        if string[i] == substring[j]:
            i += 1
            j += 1
            if j == m:
                return i - m
        else:
            if j > 0:
                j = pi[j - 1]
            else:
                i += 1
    return None
