#!/usr/bin/env python3
"""
type-annotated function concat that takes a
string a and a string b as arguments and returns their concatenation as a string.
"""


def concat(a: str, b: str) -> str:
    """
    Args: a (str): first string
          b (str): second string

    Returns: str: concatenation of a and b
    """
    return (a + b)
