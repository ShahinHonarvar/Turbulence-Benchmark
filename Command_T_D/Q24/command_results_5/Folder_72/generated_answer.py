def sum_of_divisors_in_range(n):
    return (sum(range(1, n // 2)) + sum(range(n // 2, n))) * n / 2
