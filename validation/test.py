
"""
Tests for substring search validation
"""

from typing import Callable

TEST_CASES = [
    {"string": "abcde", "substring": "bcd", "expected": 1},
    {"string": "abcde", "substring": "xyz", "expected": None},
    {"string": "ababab", "substring": "aba", "expected": 0},
    {"string": "abcde", "substring": "", "expected": None},
    {"string": "Lorem ipsum dolor sit amet...", "substring": "dolor", "expected": 12},
    {"string": "Hello, world!", "substring": "world", "expected": 7},
    {"string": "1234567890", "substring": "345", "expected": 2},
    {"string": "aaaaaaa", "substring": "aaa", "expected": 0},
    {"string": "This is a test.", "substring": "is a", "expected": 5},
    {"string": "ababcababc", "substring": "abc", "expected": 2}
]

def run_tests(algorithms: list[Callable]) -> int:
    """
    Run tests for substring search algorithms.

    Args:
        algorithms (list[Callabe]): substring search functions to evaluate

    Returns:
        int: 0 if succeeds, otherwise 1
    """
    failed = False
    for algorithm in algorithms:
        for test_case in TEST_CASES:
            actual = algorithm(string=test_case['string'], substring=test_case['substring'])
            try:
                assert actual == test_case['expected']
            except AssertionError:
                msg = f'Algorithm {algorithm.__name__} failed:\n' \
                      f'\tstring: {test_case["string"]}' \
                      f'\tsubstring: {test_case["substring"]}' \
                      f'\texpected: {test_case["expected"]}' \
                      f'\tactual: {actual}'
                print(msg)
                failed = True
    return int(failed)
