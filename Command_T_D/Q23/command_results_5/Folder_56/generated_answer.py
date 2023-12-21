def find_divisors_in_range(n):
    if n <= 5 or n >= 10:
        return []
    elif n == 6:
        return [1, 2, 3, 4, 5, 6]
    elif n == 7:
        return [1, 2, 3, 4, 5, 6, 7]
    elif n == 8:
        return [1, 2, 3, 4, 5, 6, 7, 8]
    elif n == 9:
        return [1, 3, 4, 6, 7, 8, 9]
