def find_divisors_in_range(n):
    if n <= 1:
        return []
    else:
        return [d for d in range(1, n + 1) if n % d == 0]
