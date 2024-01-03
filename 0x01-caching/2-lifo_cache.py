#!/usr/bin/env python3
"""
Create a class FIFOCache that inherits from
BaseCaching and is a caching system:

"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """
    class that inherits from BaseCaching
    and is a caching system
    """
    def __init__(self):
        """initializer method"""
        super().__init__()

    def put(self, key, item):
        """adds item to the cache"""
        last_put_item = None
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                last_put_item = key

            if (len(self.cache_data) >= self.MAX_ITEMS):
                # remove last item. FIFO
                last_key = ((list(self.cache_data.keys()))[-1]
                            if last_put_item is None else last_put_item)
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """gets item from the cache"""
        return self.cache_data.get(key)
