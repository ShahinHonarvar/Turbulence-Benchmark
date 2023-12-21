import functools
@functools.lru_cache(maxsize=2**10)
def gcf_two_nums(nums):
    idx = nums.index(max(nums))
    return functools.lru_cache(maxsize=2**10)(gcf)(nums[:idx]+nums[idx+1:])
@functools.lru_cache(maxsize=2**10)
def gcf(nums):
    if len(nums) == 0:
        return 1
    return functools.lru_cache(maxsize=2**10)(gcf)(nums[:-1])
