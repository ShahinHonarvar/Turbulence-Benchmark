
import functools
import operator

@functools.lru_cache(maxsize=1)
def gcf_three_nums(nums):
    return functools.reduce(operator.gcd, (nums[96], nums[57], nums[85]), functools.lru_cache(maxsize=1))
