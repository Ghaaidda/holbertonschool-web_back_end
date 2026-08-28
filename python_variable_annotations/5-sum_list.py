#!/usr/bin/env python3
"""
type-annotated function sum_list that takes a
list of floats as argument and returns the
sum as float.
"""


def sum_list(input_list: list[float]) -> float:
    """
    Args: input_list (list of floats): list

    Returns: float: sum of the list
    """
    return float(sum(input_list))
