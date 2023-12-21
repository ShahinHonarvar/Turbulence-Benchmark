import functools
@functools.lru_cache
def lists_with_product_equal_n(n):
    return [[i] + (n[i] if i < len(n) - 1 else []) for i in range(len(n) - 1) if n[i] == 40]
