def find_divisors_in_range(n):
    return [d for d in range(1, n + 1) if d * d <= n]
