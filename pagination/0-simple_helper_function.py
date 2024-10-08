#!/usr/bin/env python3
"""
This module provides a helper function for calculating
start and end indices for pagination based on page number and page size.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for the range
    of items to return in a list
    for pagination purposes.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index (inclusive)
        and the end index (exclusive).
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
