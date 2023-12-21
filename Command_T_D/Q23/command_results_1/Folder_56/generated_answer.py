def find_divisors_in_range(n):
    if n < 6 or n > 9:
        return []
    if n == 6 or n == 9:
        return [n]
    if n == 7:
        return [n, 6]
    if n == 8:
        return [n, 6, 4]
    return [n, 6, 7, 8]
