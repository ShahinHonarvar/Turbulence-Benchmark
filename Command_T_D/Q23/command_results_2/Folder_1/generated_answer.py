def find_divisors_in_range(n):
    if n < 10:
        return []
    elif n <= 20:
        return list(range(10, n // 2)) + [n]
    elif n <= 40:
        return list(range(10, n // 2)) + [n]
    elif n <= 55:
        return list(range(10, n // 2)) + [n]
