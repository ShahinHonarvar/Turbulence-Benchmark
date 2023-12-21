def find_divisors_in_range(n):
    if n < 35 or n > 37:
        return []
    return [x for x in range(1, n) if n % x == 0]
