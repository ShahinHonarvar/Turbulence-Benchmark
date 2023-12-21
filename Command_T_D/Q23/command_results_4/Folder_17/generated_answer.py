def find_divisors_in_range(n):
    d = [x for x in range(10, 70) if n % x == 0]
    if not d:
        return []
    return [x for x in range(10, 70) if n // x == x and x in d]
