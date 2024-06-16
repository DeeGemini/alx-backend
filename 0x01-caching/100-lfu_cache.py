#!/usr/bin/env python3
"""
LFUCache module
"""

from base_caching import BaseCaching
from collections import defaultdict, OrderedDict

class LFUCache(BaseCaching):
    """
    LFUCache class
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.frequency = defaultdict(lambda: 0)
        self.usage_order = OrderedDict()

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.frequency[key] += 1
            self.usage_order.move_to_end(key)
        else:
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order[key] = None

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Find the least frequently used key(s)
                min_freq = min(self.frequency.values())
                lfu_keys = [k for k, v in self.frequency.items() if v == min_freq]

                if len(lfu_keys) == 1:
                    lfu_key = lfu_keys[0]
                else:
                    # Use LRU among the LFU keys
                    for k in self.usage_order:
                        if k in lfu_keys:
                            lfu_key = k
                            break

                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                del self.usage_order[lfu_key]
                print("DISCARD: {}".format(lfu_key))

    def get(self, key):
        """
        Get an item by key
        """
        if key is None:
            return None
        if key not in self.cache_data:
            return None
        try:
            self.frequency[key] += 1
            self.usage_order.move_to_end(key)
            return self.cache_data[key]
        except KeyError:
            return None

# End of code
