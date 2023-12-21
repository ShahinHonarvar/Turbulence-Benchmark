def find_divisors_in_range(n):
    return [d for d in range(1, n // 2 + 1) if n % d in (0, d)]
