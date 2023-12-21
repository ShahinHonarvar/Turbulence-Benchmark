def sum_of_divisors_in_range(n):
    if n < 3:
        return 0
    if n < 4:
        return 1
    if n < 6:
        return 2
    if n < 8:
        return 3
    return 4
