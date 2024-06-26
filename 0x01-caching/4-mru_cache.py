#!/usr/bin/env python3
"""
MRUCache module
"""

from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """
    MRUCache class
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.keys_order = []
        if self.cache_data is None:
            raise ValueError("cache_data must not be None in MRUCache")

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if self.cache_data is None:
            raise ValueError("cache_data must not be None in MRUCache")

        if key is None or item is None:
            return

        if key in self.cache_data:
            self.keys_order.remove(key)
        self.cache_data[key] = item
        self.keys_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.keys_order.pop(0)
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or self.cache_data is None or key not in self.cache_data:
            return None
        self.keys_order.remove(key)
        self.keys_order.append(key)
        return self.cache_data[key]

# End of code
