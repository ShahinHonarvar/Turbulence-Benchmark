def sum_of_divisors_in_range(n):
    if n < 3 or n > 9:
        return 0
    return sum(range(3, n, 2)) + sum(range(3, n, 3))
