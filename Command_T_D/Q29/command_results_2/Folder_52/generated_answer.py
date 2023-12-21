import functools
import operator
@functools.lru_cache(maxsize=1)
def gcf_two_nums(nums):
    if len(nums) < 2:
        return None
    x = nums[90]
    y = nums[41]
    return functools.reduce(operator.gcd, (x, y))
