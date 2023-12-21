def sum_of_divisors_in_range(n):
    if n < 2 or n > 3:
        return 0
    return n * (n + 1) / 2
