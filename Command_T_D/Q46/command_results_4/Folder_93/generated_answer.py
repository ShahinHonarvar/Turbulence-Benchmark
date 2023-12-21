
import functools

@functools.lru_cache(maxsize=1)
def gcf_three_nums(lst):
    return max(gcd(lst[25], lst[76]), gcd(lst[25], lst[57]), gcd(lst[76], lst[57]))
