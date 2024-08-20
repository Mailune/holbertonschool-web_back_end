#!/usr/bin/env python3

import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension

"""
This module provides a coroutine to measure the runtime 
of executing async_comprehension four times in parallel.
"""


async def measure_runtime() -> float:
    """
    Measures the total runtime of running async_comprehension
    four times in parallel using asyncio.gather.

    Returns:
        The total runtime as a float in seconds.
    """
    start_time = time.perf_counter()

    await asyncio.gather(
        async_comprehension(), 
        async_comprehension(), 
        async_comprehension(), 
        async_comprehension()
    )

    end_time = time.perf_counter()

    return end_time - start_time
