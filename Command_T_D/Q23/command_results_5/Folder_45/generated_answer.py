def find_divisors_in_range(x):
    if x <= 3:
        return []
    if x <= 5:
        return [x, x // 2, x // 3, x // 5]
    return [x, x // 2, x // 3, x // 4, x // 5, x // 6, x // 7]
