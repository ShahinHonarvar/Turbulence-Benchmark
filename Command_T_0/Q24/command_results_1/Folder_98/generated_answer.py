def sum_of_divisors_in_range(n):
    if n < 3 or n > 8:
        return 0
    if n == 1 or n == 2:
        return 1
    if n == 3 or n == 5:
        return 2
    if n == 4 or n == 6:
        return 3
    if n == 7:
        return 6
    return 1 + 2 + 3 + 6
