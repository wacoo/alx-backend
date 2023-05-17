#!/usr/bin/env python3
''' create a class that handles cache storage and
retrival using MRU algorithm named LRUCache that
inherits from BaseCaching '''
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    ''' MRUCache class that in herits BaseCaching.
    It applies MRU algorithm to store chache '''
    def __init__(self):
        ''' initializes the MRUCache class '''
        super().__init__()
        self.mru_key = {}
        self.count = 0

    def put(self, key, item):
        ''' saves cache based on LRU algorithm '''
        if key is not None or item is not None:
            mr_key = 0
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    mr_key = max(self.mru_key, key=self.mru_key.get)
                    self.mru_key.pop(mr_key)
                    self.cache_data.pop(mr_key)
                    print('DISCARD: {}'.format(mr_key))
                self.cache_data[key] = item
                self.count += 1
                self.mru_key[key] = self.count

    def get(self, key):
        ''' return item with given key from self.cache_data '''
        if key is None or key not in self.cache_data:
            return None
        self.count += 1
        self.mru_key[key] = self.count
        return self.cache_data[key]
