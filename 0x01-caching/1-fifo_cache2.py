#!/usr/bin/env python3
''' Create a class FIFOCache that inherits from BaseCachingi
and is a caching system '''
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    ''' FIFOCache class that inherits from BaseCaching '''

    def __init__(self):
        ''' initialize the class '''
        super().__init__()
        self.cache_order = {}
        self.count = 0

    def put(self, key, item):
        ''' store cache data in FIFO order '''
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_key = min(self.cache_order, key=self.cache_order.get)
                key_pop = self.cache_order[min_key]
                if key not in self.cache_data:
                    self.cache_data.pop(key_pop)
                    self.cache_order.pop(min_key)
                    self.count -= 1
                    print('DISCARD: {}'. format(key_pop))

            self.cache_data[key] = item
            self.count += 1
            self.cache_order[self.count] = key

    def get(self, key):
        ''' return the key value from self.cache_data or None '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
