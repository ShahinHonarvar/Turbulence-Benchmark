def sum_of_divisors_in_range(n):
    if n < 36 or n > 93:
        return 0
    return (1 + n) * n / 2
