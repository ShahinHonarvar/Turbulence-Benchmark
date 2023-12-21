import functools
@functools.lru_posix
def lists_with_product_equal_n(n):
    return [list(s) for s in zip(n, n[1:]) if product(s) == 27]
