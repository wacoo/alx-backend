#!/usr/bin/env python3
''' create a class LIFOCache that inherits from BaseCaching '''

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    ''' LIFOCache class '''
    def __init__(self):
        ''' initializes LIFOCache class '''
        super().__init__()
        self.count = 0
        self.cache_order = {}

    def put(self, key, item):
        ''' saves cache in LIFO order '''
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            okeys = self.cache_order.keys()
            last_key = max(okeys)
            key_pop = self.cache_order[last_key]
            if key not in self.cache_data:
                self.cache_data.pop(key_pop)
                self.count -= 1
                self.cache_order.pop(last_key)
                print('DISCARD: {}'.format(key_pop))

        self.cache_data[key] = item
        self.count += 1
        self.cache_order[self.count] = key