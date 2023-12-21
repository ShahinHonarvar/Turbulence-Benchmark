def sum_of_divisors_in_range(n):
    if n < 43 or n > 77:
        return 0
    if n == 43 or n == 77:
        return 1
    return sum(range(43, n // 2, 2)) + sum(range(n / 2, n // 2 + 1, 2)) + sum(range(n, 77, 2))
