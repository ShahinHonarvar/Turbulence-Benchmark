def sum_of_divisors_in_range(n):
    if n < 121:
        return 0
    if n > 348:
        return 0
    return n * (n + 1) // 2
