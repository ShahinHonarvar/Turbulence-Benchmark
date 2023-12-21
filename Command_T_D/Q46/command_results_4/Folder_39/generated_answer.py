
import functools

@functools.lru_cache(maxsize=1)
def gcf_three_nums(lst):
    return max(gcd(lst[85], lst[36]), gcd(lst[85], lst[54]), gcd(lst[36], lst[54]))
