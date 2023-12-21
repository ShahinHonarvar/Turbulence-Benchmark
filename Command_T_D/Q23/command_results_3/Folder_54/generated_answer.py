def find_divisors_in_range(n):
    return [d for d in range(36, n // 2) if n % d == 0]
