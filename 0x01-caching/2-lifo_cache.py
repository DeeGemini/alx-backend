#!/usr/bin/env python3
"""
LIFOCache module
"""

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """
    LIFOCache class
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        if self.cache_data is None:
            raise ValueError("cache_data must not be None in LIFOCache")
        self.keys_order = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.keys_order.remove(key)
        self.cache_data[key] = item
        self.keys_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.keys_order.pop()
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))

    def get(self, key):
        """
        Get an item by key
        """
        if self.cache_data is None:
            return None
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

# End of code
