def sum_of_divisors_in_range(n):
    if n < 2 or n > 4:
        return 0
    return sum(range(2, n // 2 + 1)) + sum(range(n // 2, n, 2))
