#!/usr/bin/env python3
"""
type-annotated function sum_list that takes a
list of floats as argument and returns the
sum as float.
"""


from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Args: input_list (list of floats): list

    Returns: float: sum of the list
    """
    return float(sum(input_list))
