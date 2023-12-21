import functools
@functools.lru_cache(maxsize=2)
def gcf_two_nums(nums):
    return max(nums[90],nums[84])
