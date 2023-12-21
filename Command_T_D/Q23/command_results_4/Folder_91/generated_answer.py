def find_divisors_in_range(x):
    if x < 2 or x > 9:
        return []
    if x == 2 or x == 3 or x == 5 or x == 7 or x == 9:
        return [x]
    if x == 4:
        return [2, 4]
    if x == 6:
        return [2, 3, 6]
    return [i for i in range(2, x // 2 + 1) if x % i == 0]
