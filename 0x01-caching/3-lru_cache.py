#!/usr/bin/env python3
"""
LRUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict

class LRUCache(BaseCaching):
    """
    LRUCache class
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        if self.cache_data is None:
            raise ValueError("cache_data must not be None in LRUCache")
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key, _ = self.cache_data.popitem(last=False)
                print("DISCARD: {}".format(first_key))

        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if self.cache_data is None:
            return None
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]

# End of code
