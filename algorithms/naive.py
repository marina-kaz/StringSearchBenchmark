"""
Naive (brute-force) substring search algorithm

Searches for a substring in a given text by comparing
each possible substring with the target. 

Time complexity: O(m * n)
"""


def naive_search(string: str, substring: str) -> None:
    """
    Naive (brute-force) substring search algorithm

    Args:
        string (str): text in which to find a substring
        substring (str): substring to find in text

    Returns:
        Optional[int]: position at which substring matching pattern begins
                       if there is one, otherwise None

    Steps:
    1. Iterate through each character in the text.
    2. For each character, check if a substring starting at that position
       matches the target substring.
    3. Repeat until a match is found or the end of the text is reached.
    """
    if not substring:
        return None

    m = len(substring)
    n = len(string)

    for i in range(n - m + 1):
        j = 0

        while j < m:
            if string[i + j] != substring[j]:
                break
            j += 1
        if j == m:
            return i
