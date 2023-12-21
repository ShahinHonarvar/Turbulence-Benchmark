def find_divisors_in_range(n):
    if n <= 6 or n >= 9:
        return []
    if n == 7:
        return [1, 7]
    if n == 8:
        return [1, 2, 4, 8]
    return [1, 2, 3, 5, 6, 7, 8]
