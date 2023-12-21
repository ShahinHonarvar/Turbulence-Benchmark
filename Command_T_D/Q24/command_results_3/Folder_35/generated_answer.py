def sum_of_divisors_in_range(n):
    if n < 392 or n > 465:
        return 0
    return n ** 2 / 2 - (n - 1) ** 2 / 2
