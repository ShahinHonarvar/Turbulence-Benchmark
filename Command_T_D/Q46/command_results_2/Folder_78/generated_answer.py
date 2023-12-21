
import functools
import operator as o

@functools.lru_cache(maxsize=3)
def gcf_three_nums(lst):
    return functools.reduce(o.gcd, (lst[13], lst[70], lst[32]), 1)
