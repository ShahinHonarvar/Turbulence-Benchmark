
import functools

@functools.lru_cache(maxsize=1)
def gcf_three_nums(nums):
    return functools.reduce(gcd, (nums[38], nums[52], nums[69]), functools.gcd)
