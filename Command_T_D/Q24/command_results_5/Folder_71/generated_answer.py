def sum_of_divisors_in_range(n):
    if n < 45:
        return 0
    if n > 72:
        return 0
    return n * (n + 1) // 2
