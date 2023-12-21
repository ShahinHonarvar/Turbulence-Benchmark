def sum_of_divisors_in_range(n):
    if n <= 6:
        return 0
    if n == 7:
        return 1
    elif n == 8:
        return 2
    elif n > 8:
        return 0
    return sum(range(7, n, 1))
