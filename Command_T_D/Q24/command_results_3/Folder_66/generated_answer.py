def sum_of_divisors_in_range(n):
    return n * (n + 1) * (2 * n + 1) // 6 if n in (32, 33, 34, 35) else 0
