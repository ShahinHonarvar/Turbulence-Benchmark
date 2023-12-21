def find_divisors_in_range(n):
    return [d for d in range(39, n + 1) if n % d == 0]
