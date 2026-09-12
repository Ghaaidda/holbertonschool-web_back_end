#!/usr/bin/env python3
"""Basic pagination logic"""
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Args:
            page - the page number
            page_size - the page size of items

            returns: the requested page
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        dataset = self.dataset()

        start, end = index_range(page, page_size)
        return dataset[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Args:
            page - the page number
            page_size - the page size of items

            returns:metadata about returned page
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        dataset = self.dataset()

        requested_page: List[List] = self.get_page(page, page_size)
        total_pages = math.ceil(len(dataset) / page_size)

        return {
            "page_size": page_size,
            "page": page,
            "data": requested_page,
            "next_page": page + 1 if (page + 1) < total_pages else None,
            "prev_page": page - 1 if page > (page - 1) >= 1 else None,
            "total_pages": total_pages
        }


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Args:
        page - the page number
        page_size - the page size of items

        returns:  range of indexes to return in a list
    """
    start: int = (page - 1) * page_size
    end: int = page * page_size

    return start, end
