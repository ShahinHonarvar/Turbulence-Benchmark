import functools
@functools.lru_cache(maxsize=2**20)
def gcf_two_nums(nums):
    return functools.lru_cache(maxsize=2**20)(gcf)(nums[46],nums[84])
