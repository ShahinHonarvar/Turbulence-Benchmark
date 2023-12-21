def find_divisors_in_range(n):
    if n < 11 or n > 56:
        return []
    return [x for x in range(1, n // 2 + 1) if n % x == 0]
