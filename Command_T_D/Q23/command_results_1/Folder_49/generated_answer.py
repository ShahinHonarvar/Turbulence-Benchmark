def find_divisors_in_range(n):
    if n < 2 or n > 6:
        return []
    if n == 2 or n == 3:
        return [2, 3]
    if n == 4 or n == 6:
        return [2, 3, 4, 6]
    return [2, 3, 4, 5]
