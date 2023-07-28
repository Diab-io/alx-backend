#!/usr/bin/env python3
""" FIFOCache module """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ class that implements fifo caching """

    def put(self, key, item):
        """ stores the data """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_key = list(self.cache_data.keys())[0]
            del self.cache_data[discard_key]
            print(f"DISCARD: {discard_key}")

    def get(self, key):
        """ retrieves the data """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
