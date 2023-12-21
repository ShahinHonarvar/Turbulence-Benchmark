
import functools
import operator

@functools.lru_cache(maxsize=1)
def gcf_three_nums(nums):
    return functools.reduce(operator.gcd, (nums[66], nums[56], nums[92]))
