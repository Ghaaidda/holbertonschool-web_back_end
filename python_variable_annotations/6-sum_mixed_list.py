#!/usr/bin/env python3
"""
type-annotated function sum_mixed_list that
takes a list of integers and floats as argument
and returns the sum as float.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Args: imxd_lst (list of integers and floats): list

    Returns: float: sum of the list
    """
    return float(sum(mxd_lst))
