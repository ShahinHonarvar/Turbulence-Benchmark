
import functools

@functools.lru_cache(maxsize=1)
def gcf_three_nums(lst):
    return functools.reduce(gcd, (lst[85], lst[36], lst[54]))
