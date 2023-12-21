import functools
@functools.lru_cache(maxsize=1)
def lists_with_product_equal_n(n):
    return [list(range(1, n+1)) for i in range(1, n+1) if n % i == 0 and n // i == i]
