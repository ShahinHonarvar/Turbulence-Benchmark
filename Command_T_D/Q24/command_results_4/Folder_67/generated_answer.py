def sum_of_divisors_in_range(n):
    if n <= 33 or n >= 57:
        return 0
    return (n - 1) * (n - 1) * (n - 2) / 6
