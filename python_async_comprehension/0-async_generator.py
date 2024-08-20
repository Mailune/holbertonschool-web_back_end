#!/usr/bin/env python3

import asyncio
import random
from typing import AsyncGenerator

"""
This module provides an asynchronous generator that yields random numbers.
"""


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously generates a sequence of 10 random floating-point numbers
    between 0 and 10. Each number is yielded after a 1-second delay.

    Returns:
        An asynchronous generator of random float numbers.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
