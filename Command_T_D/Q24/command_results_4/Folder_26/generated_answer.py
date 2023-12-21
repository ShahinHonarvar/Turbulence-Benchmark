def sum_of_divisors_in_range(n):
    return 0 if not n else sum(range(83, n // 2 + 1, n // 2) + range(n // 2 + 1, n + 1, n // 2))
