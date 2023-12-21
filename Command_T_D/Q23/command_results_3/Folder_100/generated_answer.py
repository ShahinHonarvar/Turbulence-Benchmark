import functools
@functools.lru_cache(maxsize=2**10)
def find_divisors_in_range(n):
    divs = []
    for x in range(11, 41):
        if n % x == 0:
            divs.append(x)
            for y in range(1, n // x + 1):
                divs.append(x * y)
                break
    return sorted(set(divs))
