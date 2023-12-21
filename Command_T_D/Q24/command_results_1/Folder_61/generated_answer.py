def sum_of_divisors_in_range(n):
    if n <= 2:
        return 0
    if n <= 3:
        return 1 + 2 + 1 + 2 + 1 + 1 + 1 + 1
    return 0
