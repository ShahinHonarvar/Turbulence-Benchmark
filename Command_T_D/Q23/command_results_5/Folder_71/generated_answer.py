def find_divisors_in_range(n):
    if n <= 1:
        return []
    if n <= 45:
        return []
    elif n <= 60:
        return [x for x in range(1, n // 2 + 1) if n % x == 0]
    else:
        return [x for x in range(1, n // 2 + 1) if n % x == 0]
