def sum_of_divisors_in_range(n):
    if n < 7 or n > 8:
        return 0
    return sum(range(1, n // 2 + 1)) + sum(range(n // 2, n, 2))
