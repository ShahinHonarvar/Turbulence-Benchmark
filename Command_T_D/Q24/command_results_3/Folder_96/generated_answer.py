def sum_of_divisors_in_range(n):
    if n < 6:
        return 0
    elif n < 10:
        return n * (n + 1) / 2
    else:
        return n / 2
