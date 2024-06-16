#!/usr/bin/env python3
"""
FIFOCache module
"""

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """
    FIFOCache class
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.keys_order = [] if self.cache_data is not None else None
        if self.keys_order is None:
            raise ValueError("cache_data must not be None in FIFOCache")

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.keys_order.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = self.keys_order.pop(0)
            del self.cache_data[first_key]
            print("DISCARD: {}".format(first_key))

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

# End of code
