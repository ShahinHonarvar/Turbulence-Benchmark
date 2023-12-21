import functools
@functools.lru_cache(maxsize=10**5)
def lists_with_product_equal_n(n):
    return [a for a in range(n) if a * n == -97]
