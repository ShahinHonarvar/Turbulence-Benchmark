
import functools

@functools.lru_cache(maxsize=1)
def gcf_three_nums(lst):
    return functools.reduce(lambda a,b: a*b//gcd(a,b), (lst[21], lst[69], lst[41]), 1)
