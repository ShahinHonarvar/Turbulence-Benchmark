import functools
import operator as op
@functools.lru_cache(maxsize=1)
def gcf_two_nums(lst):
    return max(list(map(gcf, lst[429], lst[289])), default=1)
@functools.lru_cache(maxsize=1)
def gcf(num):
    if num < 2:
        return 1
    return gcf(num // 2) * 2
