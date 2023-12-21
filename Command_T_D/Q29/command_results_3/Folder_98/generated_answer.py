import functools
import operator
@functools.lru_cache(maxsize=10)
def gcf_two_nums(lst):
    return functools.reduce(operator.gcd, lst[:2])
