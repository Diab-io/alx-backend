#!/usr/bin/env python3
""" LFUCache Module """

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ Least frequency used cache class
    """
    def __init__(self):
        """ initialize """
        super().__init__()
        # stores how frequent an item was accessed
        self.frequency = {}
        # stores how recent an item was accessed
        self.queue = []

    def put(self, key, item):
        """
            stores the data and deletes the least frequently used item
            if the storage is full, if there are multiple LFU items it
            uses the LRU caching method
        """
        if key is None or item is None:
            return
        if key in self.queue:
            self.queue.remove(key)
        # adds to the cache_data
        self.cache_data[key] = item
        # increments the frequency of an item if keys exists
        # if key doesn't exist it sets it to one
        self.frequency[key] = self.frequency.get(key, 0) + 1
        # Adds a key to the queue which is used for storing
        # how recent an item was used
        self.queue.append(key)

        multiple_lru = []
        # if we have more items than the max(if storage is full)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # exclude_key was created so the newly added frequency
            # of an item which is always one is not added to the
            # calculation of the min_value as that item is fresh
            excluded_key = key
            # we filter the frequency dict to not include the
            # newly added key
            filtered_frequency = {
                key: value for key, value in
                self.frequency.items() if key != excluded_key
                }
            min_value = min(filtered_frequency.values())
            # The least_used list is created incase multiple items
            # Have the same frequency in which case we use the LRU-caching
            least_used = [
                key for key, value in self.frequency.items()
                if (value == min_value)
                ]
            if len(least_used) > 1:
                # if we have more than one items, used the same
                # amount of time
                for i in least_used:
                    if i in self.queue:
                        # we select the least_used from the queue
                        # that tracks how recent all items were used
                        # doing this we narrow it down to only least frequently
                        # used items
                        multiple_lru.append(i)
                # we delete the first item because the items because
                # we remove an item when it has been accessed and append it
                # therefore any element at the beginning of the list is the
                # least frequently used
                del self.cache_data[multiple_lru[0]]
                del self.frequency[multiple_lru[0]]
                self.queue.remove(multiple_lru[0])
            else:
                # if there is just one item we do it straightforward
                del self.cache_data[least_used[0]]
                self.queue.remove(multiple_lru)
            print(f"DISCARD {least_used[0]}")

    def get(self, key):
        """ retrieves the data """
        if key is None or key not in self.cache_data.keys():
            return None
        # since this method retrieves data when this method is called we
        # add to the vals of frequency dict, and then we remove an element from
        # the queue and append it to simulate a recently used item/cache
        self.frequency[key] += 1
        self.queue.remove(key)
        self.queue.append(key)
        return self.cache_data[key]
