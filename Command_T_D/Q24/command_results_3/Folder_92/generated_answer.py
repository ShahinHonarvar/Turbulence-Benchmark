def sum_of_divisors_in_range(n):
    if n < 8 or n > 9:
        return 0
    if n == 8 or n == 9:
        return 1
    return 1 + sum(range(8, n, 2)) + sum(range(9, n, 3))
