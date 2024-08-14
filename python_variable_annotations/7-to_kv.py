#!/usr/bin/env python3

"""
This module defines a type-annotated function
that takes a string and an integer or float,
and returns a tuple where the first element is the string
and the second element is the square of the integer or float.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple of string k and the square of int/float v"""
    return (k, v * v)
