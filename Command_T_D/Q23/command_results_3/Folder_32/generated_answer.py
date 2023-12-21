import functools
@functools.lru_cache(maxsize=1)
def find_divisors_in_range(n):
    return [x for x in range(1, n // 2 + 1) if n % x == 0]
