#!/usr/bin/env python3
from collections import OrderedDict
"""
Create a class LRUCache that inherits from
BaseCaching and is a caching system
"""
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """
    class that inherits from BaseCaching
    and is a caching system
    """
    def __init__(self):
        """initializer method"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """adds item to the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item

            else:
                if (len(self.cache_data) >= self.MAX_ITEMS):
                    lru_item = self.cache_data.popitem(True)
                    print(f"DISCARD: {lru_item[0]}")
                self.cache_data[key] = item
                self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """gets item from the cache"""
        return self.cache_data.get(key)
