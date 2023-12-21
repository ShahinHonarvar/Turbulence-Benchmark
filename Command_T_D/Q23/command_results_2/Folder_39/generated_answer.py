def find_divisors_in_range(n):
    return [d for d in range(11, n // 2 + 1, 2) if n % d == 0]
