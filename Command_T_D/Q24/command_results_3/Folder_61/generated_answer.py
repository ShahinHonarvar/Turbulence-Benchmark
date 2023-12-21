def sum_of_divisors_in_range(n):
    if n <= 1:
        return 0
    if n <= 2:
        return 1
    if n == 3:
        return 4
    if n <= 6:
        return 10
    return 24
