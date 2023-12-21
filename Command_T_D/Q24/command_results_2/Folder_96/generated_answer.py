def sum_of_divisors_in_range(n):
    if n < 6:
        return 0
    if n < 8:
        return n / 6
    return (n + 1) / 2
