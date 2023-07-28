#!/usr/bin/env python3
""" LIFOCache module """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ class that implements fifo caching """

    # stores the key of the last added item
    LAST_ITEM = ''

    def put(self, key, item):
        """
        stores the data and deletes the last item
        if storage is full
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del self.cache_data[LIFOCache.LAST_ITEM]
            print(f"DISCARD: {LIFOCache.LAST_ITEM}")
        LIFOCache.LAST_ITEM = key

    def get(self, key):
        """ retrieves the data """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
