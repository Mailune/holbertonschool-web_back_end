#!/usr/bin/env python3

"""
This module defines a type-annotated function that calculates
the sum of a list containing both integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Return the sum of a list of integers and floats"""
    sum = 0
    for i in mxd_lst:
        sum += i
    return sum
