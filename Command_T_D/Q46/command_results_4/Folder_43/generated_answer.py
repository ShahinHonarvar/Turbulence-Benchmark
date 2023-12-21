
import functools
import operator as op

@functools.lru_cache(maxsize=1)
def gcf_three_nums(lst):
    return op.gcd(lst[33], lst[78], lst[93])
