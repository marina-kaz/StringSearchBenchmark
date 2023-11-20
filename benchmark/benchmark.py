import time

import pandas as pd
from tqdm import tqdm

from typing import Callable


def time_function(func: Callable, string: str, substring: str) -> float:
  """
  Measure execution time
  """
  start = time.perf_counter()
  func(string=string, substring=substring)
  return time.perf_counter() - start


def run_bechmark(data: pd.DataFrame, algorithms: list[Callable]) -> pd.DataFrame:
    """
    Collect execution statistics
    """
    for search in algorithms:
        time_logs = []
        for i in tqdm(range(data.shape[0])):
            entry = data.iloc[i]
            string, substring = entry.string, entry.substring
            time_logs.append(time_function(search, string, substring))
        data[search.__name__] = time_logs
    return data
