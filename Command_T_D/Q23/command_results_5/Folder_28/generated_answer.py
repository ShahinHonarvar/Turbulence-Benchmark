import sys
import functools
@functools.lru_cache(maxsize=1_000_000)
def find_divisors_in_range(n):
    return [x for x in range(16, n + 1) if n % x == 0]
