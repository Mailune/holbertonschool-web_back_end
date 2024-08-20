#!/usr/bin/env python3
"""
This module provides a coroutine to measure the runtime
of executing async_comprehension four times in parallel.
"""

import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of running async_comprehension
    four times in parallel using asyncio.gather.

    Returns:
        The total runtime as a float in seconds.
    """
    result = 0
    start_time = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    result = await asyncio.gather(*tasks)
    end = time.time()
    result = end - start_time
    return result
