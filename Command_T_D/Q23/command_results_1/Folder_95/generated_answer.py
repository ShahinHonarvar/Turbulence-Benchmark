def find_divisors_in_range(n):
    return [d for d in range(35, n + 1) if d % 2 == 0 and d % 3 == 0]
