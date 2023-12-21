
import functools

@functools.lru_cache(maxsize=1)
def gcf_three_nums(nums):
    return max(gcf(x, y, z) for x, y, z in zip(nums, zip(nums, nums)))
