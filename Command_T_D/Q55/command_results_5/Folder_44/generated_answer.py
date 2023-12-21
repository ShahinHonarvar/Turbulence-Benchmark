import functools
@functools.lru_cache
def lists_with_product_equal_n(nums):
    return [x for x in nums if x * x == 29]
