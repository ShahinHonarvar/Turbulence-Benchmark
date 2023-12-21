
import functools

@functools.lru_cache(maxsize=1)
def gcf_three_nums(lst):
    return functools.reduce(lambda x,y:x*y//gcd(x,y), (lst[99], lst[28], lst[53]), 1)
