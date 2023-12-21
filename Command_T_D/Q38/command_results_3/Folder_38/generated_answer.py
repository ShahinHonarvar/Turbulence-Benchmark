import functools
import operator
@functools.lru_cache(maxsize=1)
def find_subset_of_length_n(s):
    return functools.reduce(operator.mul, (1 for x in range(n+1) if x == n or s[x] == s[n]), 1)
