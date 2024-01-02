#!/usr/bin/env python3
"""
Implement a method named get_page that takes two integer arguments
page with default value 1 and page_size with default value 10.

Use assert to verify that both arguments are integers greater than 0.
Use index_range to find the correct indexes to paginate the dataset
correctly and return the appropriate page of the dataset
(i.e. the correct list of rows).
If the input arguments are out of range for the dataset,
an empty list should be returned.

"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """func to return tuple corresponding to start
    and end index for the passed in pagination args"""

    start_index: int = (page - 1) * page_size
    end_index: int = start_index + page_size
    return (start_index, end_index)


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
        """func to get the contents of the page passed in as arg"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        self.dataset()
        index_tuple = index_range(page, page_size)
        start_index = index_tuple[0]
        end_index = index_tuple[1]
        return self.__dataset[start_index: end_index]
