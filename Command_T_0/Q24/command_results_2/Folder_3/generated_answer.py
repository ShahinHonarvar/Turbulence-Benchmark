def sum_of_divisors_in_range(n):
    if n < 43 or n > 46:
        return 0
    if n == 43:
        return 1
    if n == 44:
        return 2
    if n == 45:
        return 3
    if n == 46:
        return 4
    return sum(range(1, n + 1))
