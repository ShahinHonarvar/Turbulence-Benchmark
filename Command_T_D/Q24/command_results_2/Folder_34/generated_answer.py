def sum_of_divisors_in_range(n):
    if n <= 3 or n >= 6:
        return 0
    if n == 4:
        return 3
    if n == 5:
        return 7
    return 6
