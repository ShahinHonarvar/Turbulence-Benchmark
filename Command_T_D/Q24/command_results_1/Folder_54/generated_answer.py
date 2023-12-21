def sum_of_divisors_in_range(n):
    if n < 36:
        return 0
    elif n < 93:
        return (n - 1) * (n - 2) * (n - 3)
    else:
        return 0
