def sum_of_divisors_in_range(n):
    if n < 43 or n > 95:
        return 0
    else:
        return (n / 2) * (n + 1) / 2
