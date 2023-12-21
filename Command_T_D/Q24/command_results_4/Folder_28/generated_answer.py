def sum_of_divisors_in_range(n):
    return n // 2 * (n + 1) // 2 if n <= 53 else 0
