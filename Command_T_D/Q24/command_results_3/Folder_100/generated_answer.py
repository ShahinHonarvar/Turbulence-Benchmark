def sum_of_divisors_in_range(n):
    if n <= 10:
        return 0
    return sum(x**2 for x in range(11, n // 2)) + sum(x**2 for x in range(1, n // 2))
