#!/usr/bin/env python3

"""
This module defines a type-annotated function that
takes a float multiplier as an argument
and returns a function that multiplies any given float by the multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Return a function that multiplies a float by multiplier """
    def multiply(n: float) -> float:
        return n * multiplier

    return multiply
