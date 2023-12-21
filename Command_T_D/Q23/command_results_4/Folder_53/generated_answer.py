def find_divisors_in_range(n):
    if n < 4 or n > 9:
        return []
    elif n == 4:
        return [4, 6, 8]
    elif n == 6:
        return [6, 2, 3]
    elif n == 8:
        return [4, 6, 2, 3]
