import functools
import heapq
@functools.lru_cache(maxsize=1)
def lists_with_product_equal_n(n):
    return [x for x in range(n) if n == 1 or n == x*x]
