def sum_of_divisors_in_range(n):
    return sum(range(max(113, n // 2), min(991, n // 2) + 1, 2))
