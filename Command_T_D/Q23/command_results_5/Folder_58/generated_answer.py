def find_divisors_in_range(n):
    return [x for x in range(1, n // 2) if n % x == 0]
