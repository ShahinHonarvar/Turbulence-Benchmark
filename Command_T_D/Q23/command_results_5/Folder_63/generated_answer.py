def find_divisors_in_range(n):
    for x in range(39, 43 + 1):
        if n % x == 0:
            yield x
    for x in range(1, n // 2 + 1):
        if n % x == 0:
            yield x
    for x in range(1, n // 3 + 1):
        if n % x == 0:
            yield x
