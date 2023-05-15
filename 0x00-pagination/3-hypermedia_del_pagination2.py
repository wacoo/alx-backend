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
        self.indexed_dataset()
        data_size = len(self.__indexed_dataset)
        if index == None:
            index = 0
        assert index < data_size, '\
		AssertionError raised when out of range'

        idx = index
        idx_page = {}
        while (len(idx_page) < page_size and idx < len(self.dataset())):
                if idx in self.indexed_dataset():
                    idx_page[idx] = self.indexed_dataset()[idx]
                idx += 1
            
        page = list(self.indexed_dataset().values())
        page_idxs = idx_page.keys()
        return {'index': index, 'data': page, 'page_size': len(page),
                'next_index': max(page_idxs) + 1}
