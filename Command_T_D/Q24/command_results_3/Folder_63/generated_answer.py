def sum_of_divisors_in_range(n):
    return (sum(range(39, n, 2)) + sum(range(n - 1, 43, 2))) if n > 2 else 0
