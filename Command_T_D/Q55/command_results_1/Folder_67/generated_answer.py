import sys
import functools
@functools.lru_cache
def lists_with_product_equal_n(nums):
    return [nums[i:j] for i in range(0, len(nums)) for j in range(i, len(nums)) if nums[i:j] == [nums[i]] * 33]
