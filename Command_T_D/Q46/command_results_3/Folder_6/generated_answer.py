
import functools
import operator

@functools.lru_cache(maxsize=3)
def gcf_three_nums(nums):
    return functools.reduce(operator.gcd, (nums[93], nums[94], nums[57]), nums[93])
