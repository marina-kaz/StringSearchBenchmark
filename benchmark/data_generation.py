"""
Module for creating data
to benchmark substring search algorithm
"""
from math import ceil
import random

import pandas as pd
from tqdm import tqdm


def generate_random_string(length: int) -> str:
    """
    Generates random substring
    """
    syllable_pool = ["llili", "llu", "lla"]
    return "".join(random.choice(syllable_pool) for _ in range(length))


def generate_random_substring(string: str, substring_length: int):
    """
    Generates random substring given length
    """
    start_index = random.randint(0, len(string) - substring_length)
    return string[start_index : start_index + substring_length]


def generate_benchmark_data() -> pd.DataFrame:
    """
    Covered cases:
        * substring does not appear in the string
        * substring consisutes 30, 60 and 90 percent of the whole string
    """
    strings = []
    substrings = []
    for string_length in tqdm(range(10, 1000, 100)):
        for substring_ratio in range(0, 11):
            for _ in range(10):
                string = generate_random_string(length=string_length)
                if not substring_ratio:
                    substring = generate_random_string(length=int(len(string) * (substring_ratio / 10)))
                else:
                    substring = generate_random_substring(
                        string=string,
                        substring_length=ceil(len(string) * substring_ratio / 10),
                    )
                strings.append(string)
                substrings.append(substring)
    data = pd.DataFrame({"string": strings, "substring": substrings})
    data["string_length"] = data.string.apply(len)
    data["substring_length"] = data.substring.apply(len)
    return data
