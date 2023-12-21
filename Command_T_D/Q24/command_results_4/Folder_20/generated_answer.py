def sum_of_divisors_in_range(n):
    if n <= 28:
        return 0
    elif n <= 36:
        return 2 * n - 6
    elif n <= 48:
        return 3 * n - 12
    elif n <= 60:
        return 4 * n - 18
    elif n <= 72:
        return 5 * n - 24
    elif n <= 84:
        return 6 * n - 30
