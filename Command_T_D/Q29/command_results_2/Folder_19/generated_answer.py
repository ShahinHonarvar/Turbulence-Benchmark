import functools
@functools.lru_cache(maxsize=1)
def gcf_two_nums(nums):
    return functools.lru_cache(maxsize=1)(nums[66]) * functools.lru_cache(maxsize=1)(nums[90])
