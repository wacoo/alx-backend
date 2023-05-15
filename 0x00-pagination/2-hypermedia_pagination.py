#!/usr/bin/env python3
'''Replicate code from the previous task.

Implement a get_hyper method that takes the same arguments
(and defaults) as get_page and returns a dictionary containing
the following key-value pairs:

page_size: the length of the returned dataset page
page: the current page number
data: the dataset page (equivalent to return from previous task)
next_page: number of the next page, None if no next page
prev_page: number of the previous page, None if no previous page
total_pages: the total number of pages in the dataset as an integer
Make sure to reuse get_page in your implementation.

You can use the math module if necessary.
'''

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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        ''' given start and end index of a page return
            data in the page in hateoas format
        '''
        assert page >= 0 or page_size >= 0, '\
                AssertionError raised with negative values'
        assert page != 0 or page_size != 0, '\
                AssertionError raised with 0'
        assert type(page) == int, '\
                AssertionError raised when page and/or page_size are not ints'
        assert type(page_size) == int, '\
                AssertionError raised when page and/or page_size are not ints'
        start, end = index_range(page, page_size)
        self.dataset()
        if page == 1:
            prev = None
        else:
            prev = page - 1

        total = round(len(self.__dataset) / page_size)
        if page >= total:
            nxt = None
        else:
            nxt = page + 1
        return {'page_size': page_size, 'page': page,
                'data': self.__dataset[start:end],
                'next_page': nxt, 'prev_page': prev,
                'total_pages': total}


def index_range(page: int, page_size: int) -> Tuple[int]:
    ''' return a tuple of start and end index of the last page '''
    start = 0
    end = start + page_size
    for i in range(page):
        if i > 0:
            start = end
            end = start + page_size
    return (start, end)
