#!/usr/bin/env python3

"""
Function that measures the total execution time for wait_n(n, max_delay)
and returns the average time per coroutine.
"""

import asyncio
import random
from typing import List
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay),
    and return the average time per coroutine.

    Parameters:
    n (int): Number of coroutines to spawn.
    max_delay (int): Maximum delay for each coroutine.

    Returns:
    float: The average time per coroutine.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()

    total_time = end - start
    return total_time / n
