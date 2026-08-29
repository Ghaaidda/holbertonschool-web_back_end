#!/usr/bin/env python3
"""
type-annotated function element_length
that takes a list and returns the length.
"""


from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Args: lst (list of numbers): list

    Returns: list: length of each elements
    """
    return [(i, len(i)) for i in lst]
