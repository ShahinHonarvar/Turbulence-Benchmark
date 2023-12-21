def find_divisors_in_range(n):
    if n < 403 or n > 514:
        return []
    return [x for x in range(1, n + 1) if n % x == 0 and x >= 403 and x <= 514]
