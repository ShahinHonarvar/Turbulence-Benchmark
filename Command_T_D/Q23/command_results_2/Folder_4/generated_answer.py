def find_divisors_in_range(n):
    if n <= 47:
        return []
    elif n <= 59:
        return list(range(48, n+1, 1))
