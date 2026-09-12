#!/usr/bin/env python3
"""
This module implements a pagination technique using 
the page and the page size parameters only.
"""


def index_range(page, page_size):
    """
    Args:
        page - the page number
        page_size - the page size of items

        returns:  range of indexes to return in a list
    """
    start = (page - 1) * page_size
    end = page * page_size
    return start, end