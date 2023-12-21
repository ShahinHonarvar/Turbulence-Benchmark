import functools
import operator
@functools.lru_cache(maxsize=1)
def gcf_two_nums(lst):
    idx_86, idx_89 = lst.index(max(lst)), lst.index(min(lst))
    return operator.gcd(lst[idx_86], lst[idx_89])
