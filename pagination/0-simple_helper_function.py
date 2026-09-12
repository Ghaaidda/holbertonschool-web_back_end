#!/usr/bin/env python3
"""
This module implements a pagination technique using 
the page and the page size parameters only.
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int,int]:
    """
    Args:
        page - the page number
        page_size - the page size of items

        returns:  range of indexes to return in a list
    """
    start: int = (page - 1) * page_size
    end: int = page * page_size

    return start, end
