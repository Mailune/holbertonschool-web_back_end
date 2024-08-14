#!/usr/bin/env python3

"""
This module defines a type-annotated function that takes a list of strings as input
and returns a list of tuples.
Each tuple contains a string and its length.
"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence])\
        -> List[Tuple[Sequence, int]]:
    """Return a list of tuples where each tuple’s first element is string"""
    return [(i, len(i)) for i in lst]
