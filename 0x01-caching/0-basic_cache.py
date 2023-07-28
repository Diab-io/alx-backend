#!/usr/bin/env python3
""" BasicCache module """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ A class with methods for storing data and retrieving """
    def put(self, key, item):
        """ stores the data """
        if key == None or item == None:
            return
        self.cache_data[key] = item
    
    def get(self, key):
        """ retrieves the data """
        if key == None or key not in self.cache_data:
            return None
        return self.cache_data[key]
