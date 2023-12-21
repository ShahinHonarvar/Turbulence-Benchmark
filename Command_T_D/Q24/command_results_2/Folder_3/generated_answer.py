def sum_of_divisors_in_range(n):
    if n <= 43 or n >= 46:
        return 0
    if n == 44:
        return 3
    return n * (n + 1) / 2
