import functools
import operator
@functools.lru_cache(maxsize=1_000_000)
def find_divisors_in_range(n):
    return [x for x in range(33, n // 2 + 1, 2) if n % x == 0]
