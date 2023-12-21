def sum_of_divisors_in_range(n):
    if n < 8 or n > 9:
        return 0
    return sum(range(8, n // 2 + 1, 2)) + sum(range(n // 2, n, 2))
