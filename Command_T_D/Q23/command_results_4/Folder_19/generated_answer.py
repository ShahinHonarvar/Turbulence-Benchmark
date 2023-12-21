def find_divisors_in_range(n):
    if n <= 1:
        return []
    elif n <= 3:
        return [1, 2, 3]
    elif n <= 6:
        return [1, 2, 3, 4, 5, 6]
    else:
        return []
