import functools
@functools.lru_cache(maxsize=2)
def gcf_two_nums(lst):
    return functools.reduce(lambda a,b:a*b//gcd(a,b), lst[:2])
