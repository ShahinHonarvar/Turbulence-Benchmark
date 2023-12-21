def find_divisors_in_range(x):
    res = []
    for i in range(x, x//2 + 1, -1):
        if x % i == 0:
            res.append(i)
            res.append(x//i)
    return res if res else []
