def sum_of_divisors_in_range(n):
    return sum(d for d in range(5, n + 1) if d * d <= n)
