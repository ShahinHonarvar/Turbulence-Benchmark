def find_divisors_in_range(x):
    if x <= 120 or x > 349:
        return []
    res = []
    for y in range(x, 120, -1):
        if x % y == 0:
            res.append(y)
            if y != x:
                res.append(x // y)
    return res
