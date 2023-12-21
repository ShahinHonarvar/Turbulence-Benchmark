def sum_of_divisors_in_range(n):
    if n < 4 or n > 8:
        return 0
    return sum(range(4, n, 2)) + sum(range(3, n, 2))
