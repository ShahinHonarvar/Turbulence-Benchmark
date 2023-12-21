
import functools
import operator

@functools.lru_cache(maxsize=10**5)
def gcf_three_nums(nums):
    return functools.reduce(operator.gcd, (nums[66], nums[90], nums[27]))
