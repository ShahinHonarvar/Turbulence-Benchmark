def sum_of_divisors_in_range(n):
    if n < 43 or n > 77:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if n == 4:
        return 6
    if n == 5:
        return 10
    if n == 6:
        return 16
    if n == 7:
        return 22
    return 2 * n - 1
