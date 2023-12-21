def find_divisors_in_range(n):
    if n <= 50 or n >= 84:
        return []
    for x in range(1, int(n ** .5) + 1):
        if n % x == 0:
            yield x
            if x * x != n:
                yield n // x
    yield n
