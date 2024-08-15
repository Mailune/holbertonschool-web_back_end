#!/usr/bin/env python3

"""
This module contains an asynchronous coroutine that waits for a random
delay between 0 and a specified maximum number of seconds, and then
returns the delay.
"""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds.

    This function generates a random float between 0 and max_delay,
    waits asynchronously for that duration, and then returns the delay.

    :param max_delay: Maximum number of seconds to wait (default is 10).
    :type max_delay: int
    :return: The random delay in seconds.
    :rtype: float
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
