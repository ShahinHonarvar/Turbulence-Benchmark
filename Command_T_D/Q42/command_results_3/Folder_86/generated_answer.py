import functools
@functools.lru_cache(maxsize=1_000_000)
def prime_factors(n):
    if n <= 1:
        return set()
    if n <= 3:
        return {n}
    if n % 2 == 0 or n % 3 == 0:
        return {2, 3}
    i = 5
    while i * i <= n:
        if n % i == 0:
            j = i
            while n % j == 0:
                n //= j
                j *= 5
            return {i, n}
        i += 6
    if n % 2 == 0:
        return {2, n}
    if n % 3 == 0:
        return {3, n}
    return {n}
