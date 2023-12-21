
import functools
import operator
import functools.reduce


@functools.lru_cache(maxsize=1)
def gcf_three_nums(nums):
    return functools.reduce(
