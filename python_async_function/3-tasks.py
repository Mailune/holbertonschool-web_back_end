#!/usr/bin/env python3

"""Function that takes an integer max_delay and returns an asyncio.Task"""

import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Function that takes an integer max_delay and returns an asyncio.Task.

    Args:
    max_delay (int): Maximum delay value to be passed to the wait_random coroutine.

    Returns:
    asyncio.Task: An asyncio.Task object that schedules the wait_random coroutine to be run concurrently.
    """
    return asyncio.create_task(wait_random(max_delay))
