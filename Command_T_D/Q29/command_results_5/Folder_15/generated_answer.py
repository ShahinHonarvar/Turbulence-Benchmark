import functools
@functools.lru_cache(maxsize=2)
def gcf_two_nums(nums):
    return 1 if nums[0] == nums[1] else nums[0] // gcf_two_nums(nums[1:])
