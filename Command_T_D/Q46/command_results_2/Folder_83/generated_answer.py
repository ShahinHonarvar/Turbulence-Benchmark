
import functools

@functools.lru_cache(maxsize=1)
def gcf_three_nums(lst):
    return max(gcd(x, y) for x, y in zip(lst[56], lst[54]) for gcd in zip(x, y))
