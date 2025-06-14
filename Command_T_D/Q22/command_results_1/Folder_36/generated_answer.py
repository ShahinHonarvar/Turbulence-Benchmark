import functools
@functools.lru_cache(maxsize=338)
def find_sum_of_multiples(n):
    return sum(range(1, n+1, n))
