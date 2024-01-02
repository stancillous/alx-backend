#!/usr/bin/env python3
"""
Implement a get_hyper method that takes the same arguments
(and defaults) as get_page and returns a dictionary
containing the following key-value pairs:

page_size: the length of the returned dataset page
page: the current page number
data: the dataset page (equivalent to return from previous task)
next_page: number of the next page, None if no next page
prev_page: number of the previous page, None if no previous page
total_pages: the total number of pages in the dataset as an integer
Make sure to reuse get_page in your implementation.

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
    
    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        func to return a dict containing the following key-value pairs
        """
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if page_size < len(self.dataset()) else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }

server = Server()

print(server.get_hyper(1, 2))
print("---")
print(server.get_hyper(2, 2))
print("---")
print(server.get_hyper(100, 3))
print("---")
print(server.get_hyper(3000, 100))