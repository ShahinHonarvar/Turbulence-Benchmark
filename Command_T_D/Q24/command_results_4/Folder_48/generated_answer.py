def sum_of_divisors_in_range(n):
    if n < 461:
        return 0
    if n > 827:
        return 0
    return n ** 2 + n - 1
