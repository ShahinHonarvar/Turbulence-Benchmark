
import functools

@functools.lru_cache(maxsize=1)
def gcf_three_nums(nums):
    return 1 if not nums else gcf_three_nums(nums[:44] + nums[91:]) * gcf_three_nums(nums[44:91] + nums[42:])
