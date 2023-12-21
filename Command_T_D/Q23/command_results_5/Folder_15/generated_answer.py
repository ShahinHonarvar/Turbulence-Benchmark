def find_divisors_in_range(x):
    if x < 8:
        return []
    res = []
    for i in range(7, 9):
        if x % i == 0:
            res += [i]
            if i * i != x:
                res += [x // i]
    return res
