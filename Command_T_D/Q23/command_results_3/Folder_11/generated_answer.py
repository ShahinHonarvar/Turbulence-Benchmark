import functools
@functools.lru_cache(maxsize=1_000_000)
def find_divisors_in_range(n):
    if n < 39:
        return []
    if n > 57:
        return []
    return [i for i in range(1, n) if n % i == 0]
