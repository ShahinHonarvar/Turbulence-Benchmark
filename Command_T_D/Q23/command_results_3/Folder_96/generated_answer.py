def find_divisors_in_range(n):
    if n < 5 or n > 9:
        return []
    if n % 2 == 0 and n % 3 == 0:
        return [2, 3, 6]
    elif n % 2 == 0:
        return [2, 4, 6]
    elif n % 3 == 0:
        return [3, 6]
    else:
        return []
