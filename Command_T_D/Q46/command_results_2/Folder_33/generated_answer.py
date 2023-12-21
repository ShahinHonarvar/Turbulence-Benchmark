
import functools

@functools.lru_cache(maxsize=1_000_000)
def gcf_three_nums(lst):
    return functools.reduce(lambda a, b: a * b // gcd(a, b), lst[252], a=lst[149], b=lst[564])
