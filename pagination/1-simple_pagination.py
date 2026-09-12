#!/usr/bin/env python3
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
