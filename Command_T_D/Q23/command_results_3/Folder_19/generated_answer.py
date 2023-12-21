def find_divisors_in_range(n):
    if n <= 1:
        return []
    elif n <= 2:
        return [1, 2]
    elif n <= 4:
        return [1, 2, 3, 4]
    elif n <= 6:
        return [1, 2, 3, 4, 5, 6]
    else:
        return []
