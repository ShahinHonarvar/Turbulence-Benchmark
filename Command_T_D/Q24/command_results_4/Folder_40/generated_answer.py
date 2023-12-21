def sum_of_divisors_in_range(n):
    if n <= 2:
        return 1
    elif n <= 4:
        return n + 1
    elif n <= 6:
        return n * (n + 1) // 2
    else:
        return n * (n + 1) * (2 * n + 1) / 6
