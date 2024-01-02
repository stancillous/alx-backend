#!/usr/bin/env python3
"""
Create a class BasicCache that inherits
from BaseCaching and is a caching system:

"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    inherits from BaseCaching and is a caching system
    """
    def put(self, key, item):
        """func to add item to the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """gets item from the cache"""
        return self.cache_data.get(key)
