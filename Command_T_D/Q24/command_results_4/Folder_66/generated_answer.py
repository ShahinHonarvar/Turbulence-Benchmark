def sum_of_divisors_in_range(n):
    return sum(range(32, n + 1, 2) if n % 2 == 1 else range(32, n // 2 + 1, 2))
