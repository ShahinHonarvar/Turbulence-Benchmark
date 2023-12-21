
import functools

@functools.lru_cache(maxsize=1)
def gcf_three_nums(lst):
    return functools.reduce(lambda a,b:gcd(a,b), (lst[66], lst[56], lst[92]))
