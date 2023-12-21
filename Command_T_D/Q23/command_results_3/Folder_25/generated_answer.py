def find_divisors_in_range(n):
    if n <= 85:
        return [x for x in range(84, n + 1) if n % x == 0]
    else:
        return []
