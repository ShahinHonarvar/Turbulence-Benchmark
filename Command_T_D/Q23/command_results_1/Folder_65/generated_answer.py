def find_divisors_in_range(n):
    if n <= 46 or n >= 65:
        return []
    else:
        return [x for x in range(46, n + 1, 1) if n % x == 0]
