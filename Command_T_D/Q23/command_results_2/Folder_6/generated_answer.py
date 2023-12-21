def find_divisors_in_range(n):
    if n < 58 or n > 90:
        return []
    for d in range(2, int(n ** .5) + 1):
        if n % d == 0:
            yield d
            if d * d != n:
                yield n // d
    if n % 2 == 0 and n % 3 == 0:
        yield 2
    if n % 2 == 0:
        yield 3
