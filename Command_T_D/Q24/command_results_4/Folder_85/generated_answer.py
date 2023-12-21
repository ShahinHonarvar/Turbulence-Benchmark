def sum_of_divisors_in_range(n):
    if n < 2:
        return 0
    if n <= 4:
        return n / 2 + n / 3
    return 0
