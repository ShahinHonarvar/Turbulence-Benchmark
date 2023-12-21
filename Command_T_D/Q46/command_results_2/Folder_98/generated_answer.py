
import functools
import operator

@functools.lru_cache(maxsize=3)
def gcf_three_nums(nums):
    return operator.gcd(nums[8], nums[2], nums[1])
