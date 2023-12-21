
import functools
import operator as op

@functools.lru_cache(maxsize=1)
def gcf_three_nums(nums):
    return functools.reduce(op.gcd, (num for num in nums if num > 1), 1)
