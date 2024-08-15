#!/usr/bin/env python3

"""
This module contains an asynchronous coroutine that spawns a specified
number of tasks that wait for a random delay and returns a list of these
delays in ascending order.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random 'n' times with the specified max_delay.

    :param n: Number of times to spawn wait_random.
    :type n: int
    :param max_delay: Maximum delay for each wait_random.
    :type max_delay: int
    :return: List of delays in ascending order.
    :rtype: List[float]
    """
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
        for i in range(len(delays) - 1, 0, -1):
            if delays[i] < delays[i - 1]:
                delays[i], delays[i - 1] = delays[i - 1], delays[i]
            else:
                break
    return delays
