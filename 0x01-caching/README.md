# Caching Systems

## Description

This project involves implementing various caching systems using Python. Each task focuses on a different caching strategy, and all classes must inherit from a base class `BaseCaching`. The goal is to manage the cache efficiently while adhering to different caching algorithms.

### Key Concepts:

1. **Matrix Representation in Python:**
   - Understanding how dictionaries are used to represent cache storage.
   - Accessing and modifying elements in the cache.

2. **In-place Operations:**
   - Performing operations on data without creating a copy of the data structure.
   - Minimizing space complexity by modifying the cache in place.

3. **Caching Algorithms:**
   - Implementing different caching strategies (Basic, FIFO, LIFO, LRU, LFU, MRU).

4. **Nested Loops and Data Structures:**
   - Using nested loops to iterate through cache data.
   - Utilizing data structures like lists, dictionaries, and `OrderedDict` to manage cache operations.

## Tasks

### Task 0: Basic Dictionary

Create a class `BasicCache` that inherits from `BaseCaching` and is a caching system with no limit.

### Task 1: FIFO Caching

Create a class `FIFOCache` that inherits from `BaseCaching` and implements the First In First Out (FIFO) caching algorithm.

### Task 2: LIFO Caching

Create a class `LIFOCache` that inherits from `BaseCaching` and implements the Last In First Out (LIFO) caching algorithm.

### Task 3: LRU Caching

Create a class `LRUCache` that inherits from `BaseCaching` and implements the Least Recently Used (LRU) caching algorithm.

### Task 4: MRU Caching

Create a class `MRUCache` that inherits from `BaseCaching` and implements the Most Recently Used (MRU) caching algorithm.

### Task 5: LFU Caching

Create a class `LFUCache` that inherits from `BaseCaching` and implements the Least Frequently Used (LFU) caching algorithm. If there are multiple items with the same frequency, discard the least recently used one.

## Usage

### BaseCaching Class

```python
class BaseCaching():
    MAX_ITEMS = 4

    def __init__(self):
        self.cache_data = {}

    def print_cache(self):
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        raise NotImplementedError("get must be implemented in your cache class")

### Example Usage
- BasicCache
from basic_cache import BasicCache

cache = BasicCache()
cache.put("A", "Item A")
print(cache.get("A"))  # Output: Item A

- FIFOCache
from fifo_cache import FIFOCache

cache = FIFOCache()
cache.put("A", "Item A")
cache.put("B", "Item B")
cache.put("C", "Item C")
cache.put("D", "Item D")
cache.put("E", "Item E")
# Output: DISCARD: A

- LIFOCache
from lifo_cache import LIFOCache

cache = LIFOCache()
cache.put("A", "Item A")
cache.put("B", "Item B")
cache.put("C", "Item C")
cache.put("D", "Item D")
cache.put("E", "Item E")
# Output: DISCARD: E

- LRUCache
from lru_cache import LRUCache

cache = LRUCache()
cache.put("A", "Item A")
cache.put("B", "Item B")
cache.put("C", "Item C")
cache.put("D", "Item D")
cache.get("A")
cache.put("E", "Item E")
# Output: DISCARD: B

- MRUCache
from mru_cache import MRUCache

cache = MRUCache()
cache.put("A", "Item A")
cache.put("B", "Item B")
cache.put("C", "Item C")
cache.put("D", "Item D")
cache.get("D")
cache.put("E", "Item E")
# Output: DISCARD: D

- LFUCache
from lfu_cache import LFUCache

cache = LFUCache()
cache.put("A", "Item A")
cache.put("B", "Item B")
cache.put("C", "Item C")
cache.put("D", "Item D")
cache.get("A")
cache.get("A")
cache.put("E", "Item E")
# Output: DISCARD: B

### Author
-- Nontuthuzelo Ngwenya
-- Github: DeeGemini

### License
-- None
