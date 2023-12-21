
import functools
import operator

@functools.lru_cache(maxsize=1)
def gcf_three_nums(nums):
    return functools.reduce(operator.gcd, (num for num in nums if num))
