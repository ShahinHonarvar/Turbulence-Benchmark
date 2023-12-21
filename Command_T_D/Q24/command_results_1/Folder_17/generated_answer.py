def sum_of_divisors_in_range(n):
    if n < 10:
        return 0
    if n > 69:
        return 0
    return n * (n - 1) / 2
