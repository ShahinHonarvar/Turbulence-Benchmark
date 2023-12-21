def sum_of_divisors_in_range(n):
    for d in range(5, 8):
        if n % d == 0:
            return d + n / d
    return 0
