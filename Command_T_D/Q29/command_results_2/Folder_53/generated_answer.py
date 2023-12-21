import functools
import operator
@functools.lru_cache(maxsize=2)
def gcf_two_nums(nums):
    return functools.reduce(operator.gcd, nums[:28], nums[28:])
