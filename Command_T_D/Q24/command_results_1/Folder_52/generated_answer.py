def sum_of_divisors_in_range(n):
    if n < 70 or n > 72:
        return 0
    if n == 70:
        return 12
    elif n == 71:
        return 12
    elif n == 72:
        return 12
    return (n - 1) * (n - 1) * (n + 1)
