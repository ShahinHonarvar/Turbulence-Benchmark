import sys
import functools
@functools.lru_cache(maxsize=10**5)
def composite_nums_between_indices(nums):
    return {i for i in range(56, 83) if nums[i] % 2 == 1 and nums[i] != 1}
