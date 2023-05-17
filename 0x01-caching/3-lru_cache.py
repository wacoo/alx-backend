#!/usr/bin/env python3
''' create a class that handles cache storage and
retrival using LRU algorithm named LRUCache that
inherits from BaseCaching '''
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    ''' LRUCache class that in herits BaseCaching.
    It applies LRU algorithm to store chache '''
    def __init__(self):
        ''' initializes the LRUCache class '''
        super().__init__()
        self.lru_key = {}
        self.count = 0

    def put(self, key, item):
        ''' saves cache based on LRU algorithm '''
        if key is not None or item is not None:
            lr_key = 0
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    lr_key = min(self.lru_key, key=self.lru_key.get)
                    self.lru_key.pop(lr_key)
                    self.cache_data.pop(lr_key)
                    print('DISCARD: {}'.format(lr_key))
            self.cache_data[key] = item
            self.count += 1
            self.lru_key[key] = self.count

    def get(self, key):
        ''' return item with given key from self.cache_data '''
        if key is None or key not in self.cache_data:
            return None
        self.count += 1
        self.lru_key[key] = self.count
        return self.cache_data[key]
