#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Tuple, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        ''' return a dictionary of hateoes page info '''

        assert index >= 0, '\
                AssertionError raised when out of range'
        assert index < len(self.indexed_dataset()), '\
                AssertionError raised when out of range'

        idataset = self.indexed_dataset()
        idx = index
        indexed_pg = {}
        keys = self.indexed_dataset().keys()
        while (len(indexed_pg) < page_size and idx < len(self.dataset())):
            if idx in idataset:
                indexed_pg[idx] = idataset[idx]
            idx += 1
        page = list(indexed_pg.values())
        indexes = indexed_pg.keys()

        return {'index': index, 'data': page, 'page_size': len(page),
                'next_index': max(indexes) + 1}
