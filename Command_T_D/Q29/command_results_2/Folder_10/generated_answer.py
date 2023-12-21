import functools
import operator
import fractions
@functools.lru_cache(maxsize=2)
def gcf_two_nums(nums):
    return fractions.gcd(nums[15], nums[99])
