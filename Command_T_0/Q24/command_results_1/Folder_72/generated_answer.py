def sum_of_divisors_in_range(n):
    return sum(range(32, n // 2 + 1, 2)) + sum(range(n // 2, n, 2))
