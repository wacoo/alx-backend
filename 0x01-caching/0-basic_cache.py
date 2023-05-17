#!/usr/bin/env python3
''' Create a class BasicCache that inherits from BaseCaching
and is a caching system '''

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    ''' BasicCache class that inherits from BaseCaching '''
    def put(self, key, item):
        ''' assign valkue to self.cache_item '''
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        ''' return the value of self.cache_data[key] or None '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
