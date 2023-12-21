def sum_of_divisors_in_range(n):
    if n < 2 or n > 6:
        return 0
    return n / 2 + (n + 1) / 2
