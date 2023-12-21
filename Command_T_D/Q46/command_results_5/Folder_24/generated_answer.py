
import functools

@functools.lru_cache(maxsize=1)
def gcf_three_nums(lst):
    return 1 / functools.reduce(lambda x,y: x * y // gcd(x,y), lst[18:], lst[18])
