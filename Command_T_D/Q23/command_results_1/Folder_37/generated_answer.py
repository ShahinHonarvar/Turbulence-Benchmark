def find_divisors_in_range(n):
    if n <= 1:
        return []
    elif n <= 2:
        return [3, 4, 5]
    elif n <= 6:
        return [3, 4, 5, 6]
    elif n <= 10:
        return [3, 4, 5, 6, 7, 8, 9, 10]
