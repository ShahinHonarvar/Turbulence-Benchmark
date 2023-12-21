def find_divisors_in_range(n):
    if n < 2 or n > 3:
        return []
    elif n == 2 or n == 3:
        return [n]
    elif n == 4:
        return [2, 3]
    else:
        return [2, 3, n // 2, n // 3, n // 2 - 1, n // 3 - 1]
