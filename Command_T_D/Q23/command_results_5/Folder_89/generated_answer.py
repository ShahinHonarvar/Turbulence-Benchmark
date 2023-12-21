def find_divisors_in_range(n):
    return [x for x in range(14, n // 2 + 1, 2) if n % x == 0] + [x for x in range(14, n // 3 + 1, 3) if n % x == 0]
