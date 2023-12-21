def find_divisors_in_range(n):
    if n < 4 or n > 8:
        return []
    return [x for x in range(1, n // 2) if n % x == 0]
