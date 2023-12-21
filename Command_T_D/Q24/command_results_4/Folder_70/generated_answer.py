def sum_of_divisors_in_range(n):
    return sum(range(n, n // 2, -1) + range(n, n // 3, -1))
