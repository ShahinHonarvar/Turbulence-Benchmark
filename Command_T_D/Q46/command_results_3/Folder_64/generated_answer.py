
import functools
import math

@functools.lru_cache(maxsize=1)
def gcf_three_nums(nums):
    return math.gcd(nums[0], math.gcd(nums[8], nums[3]))
