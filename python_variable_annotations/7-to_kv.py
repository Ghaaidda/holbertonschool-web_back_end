#!/usr/bin/env python3
"""
type-annotated function to_kv that
takes a string k and an int OR float v
and returns a tuple of k and square of v.
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Args: k (str): string
          v (int or float): number

    Returns: tuple: tuple of k and suqare of v
    """

    return (k, v * v)
