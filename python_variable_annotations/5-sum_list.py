#!/usr/bin/env python3

"""
This module defines a type-annotated function that
calculates the sum of a list of floats.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Return the sum of a list of floats """
    sum: float = 0
    for i in input_list:
        sum += i
    return sum
