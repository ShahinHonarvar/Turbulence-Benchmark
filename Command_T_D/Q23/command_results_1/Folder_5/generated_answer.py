def find_divisors_in_range(n):
    return [d for d in range(7, n, 2) if n % d == 0]
