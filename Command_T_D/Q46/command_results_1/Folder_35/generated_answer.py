
import functools

@functools.lru_cache(maxsize=10**6)
def gcf_three_nums(lst):
    return functools.reduce(lambda x,y:x*y//gcd(x,y), lst[:3])
