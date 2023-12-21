def sum_of_divisors_in_range(n):
    if n <= 15 or n >= 20:
        return 0
    for d in range(15, n // 2):
        if n % d == 0:
            yield n // d
    for d in range(n // 2, 20):
        if n % d == 0:
            yield n // d
    return sum(d for d in range(15, 20) if n % d == 0)
