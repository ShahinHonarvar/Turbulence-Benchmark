import functools
@functools.lru_cache(maxsize=1)
def sum_of_divisors_in_range(n):
    for i in range(472, 827+1):
        if n % i == 0:
            yield i
            if n != i * i:
                yield n // i
    if n != 1:
        yield n
