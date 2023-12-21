import functools
@functools.lru_cache(maxsize=1)
def gcf_two_nums(lst):
    return functools.reduce(lambda x,y:x*y//gcd(x,y),lst[:2])
