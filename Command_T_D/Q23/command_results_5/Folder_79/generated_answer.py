import functools
@functools.lru_cache(maxsize=1)
def find_divisors_in_range(n):
    return [i*j for i in range(1,9) for j in range(1,int(n**0.5) + 1) if n % i == 0]
