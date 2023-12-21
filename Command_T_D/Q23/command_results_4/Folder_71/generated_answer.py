def find_divisors_in_range(n):
    if n < 45 or n > 72:
        return []
    return [d for d in range(1, n + 1) if n % d == 0 and d in range(45, 73)]
