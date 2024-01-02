#!/usr/bin/env python3
"""

"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
    class that inherits from BaseCaching
    and is a caching system
    """
    def __init__(self):
        """initializer method"""
        super().__init__()

    def put(self, key, item):
        """adds item to the cache"""
        if key is not None and item is not None:
            if (len(self.cache_data) >= self.MAX_ITEMS):
                # remove first item. FIFO
                first_key = (list(self.cache_data.keys()))[0]
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """gets item from the cache"""
        return self.cache_data.get(key)
