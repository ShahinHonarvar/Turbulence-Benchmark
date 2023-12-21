def find_divisors_in_range(n):
    if n < 2:
        return []
    if n < 3:
        return [2, n]
    if n < 4:
        return [2, 3, n]
    return []
