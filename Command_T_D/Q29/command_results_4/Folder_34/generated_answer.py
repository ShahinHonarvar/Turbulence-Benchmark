import functools
@functools.lru_cache(maxsize=1)
def gcf_two_nums(nums):
    return gcf(nums[60],nums[64])
