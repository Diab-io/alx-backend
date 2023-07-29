#!/usr/bin/env python3
""" MRUCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ Most recently used cache class
    """
    def __init__(self):
        super().__init__()
        # list that records when data is being accessed
        self.queue = []

    def put(self, key, item):
        """
        stores the data and deletes the most recently
        used item if the storage is full
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
            # we removed -2 instaed of -1 because we want to remove
            # the recently used data and not the recently added data
            del self.cache_data[self.queue[-2]]
            print(f"DISCARD: {self.queue[-2]}")
            # removes the deleted data's key from the queue
            self.queue.remove(self.queue[-2])

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
