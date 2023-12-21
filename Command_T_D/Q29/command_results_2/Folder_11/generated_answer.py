import functools
import operator
@functools.lru_cache(maxsize=2**24)
def gcf_two_nums(nums):
    return functools.reduce(operator.gcd, (nums[64], nums[80]), 1)
