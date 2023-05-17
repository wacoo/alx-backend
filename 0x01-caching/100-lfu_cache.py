#!/usr/bin/env python3
''' create a class LFUCache that inherits from BaseCaching '''

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    ''' LFUCache class '''
    def __init__(self):
        ''' initializes LFUCache class '''
        super().__init__()
        self.cache_order = {}

    def put(self, key, item):
        ''' saves cache in LFU order '''
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            key_pop = min(self.cache_order, key=self.cache_order.get)
            if key not in self.cache_data:
                self.cache_data.pop(key_pop)
                self.cache_order.pop(key_pop)
                print('DISCARD: {}'.format(key_pop))

        self.cache_data[key] = item
        if key not in self.cache_order:
            self.cache_order[key] = 1
        else:
            self.cache_order[key] += 1

    def get(self, key):
        ''' get cache from self.cache_data with key '''
        if key is None or key not in self.cache_data:
            return None

        if key not in self.cache_order:
            self.cache_order[key] = 1
        else:
            self.cache_order[key] += 1

        return self.cache_data[key]
