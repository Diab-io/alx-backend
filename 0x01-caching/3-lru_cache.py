#!/usr/bin/env python3
""" LRUCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ Least recently used cache class
    """
    def __init__(self):
        super().__init__()
        # list that records when data is being accessed
        self.queue = []

    def put(self, key, item):
        """
        stores the data and deletes the least used item
        if the storage is full
        """
        if key is None or item is None:
            return
        if key in self.queue:
            # To avoid recording duplicate keys on the queue
            # we delete an already existing key
            self.queue.remove(key)
        self.queue.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # recently used data is stored at the end
            # least recently used is stored at the beginning
            del self.cache_data[self.queue[0]]
            print(f"DISCARD: {self.queue[0]}")
            # removes the deleted data's key from the queue
            self.queue.pop(0)

    def get(self, key):
        """ retrieves the data """
        if key is None or key not in self.cache_data.keys():
            return None
        # when a data is accessed with this method
        # we remove the key from whatever position it is
        # on the queue an add it at the end
        self.queue.remove(key)
        self.queue.append(key)
        return self.cache_data[key]
