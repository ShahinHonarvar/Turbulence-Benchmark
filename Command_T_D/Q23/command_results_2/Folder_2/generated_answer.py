def find_divisors_in_range(n):
    if n <= 315:
        return []
    elif n <= 955:
        return [(i, n // i) for i in range(1, n + 1) if n % i == 0]
    else:
        return []
