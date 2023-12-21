def find_divisors_in_range(n):
    res = []
    for i in range(43, n // 2, 2):
        if n % i == 0:
            res.append(i)
            res.append(n // i)
    if n % 2 == 0:
        res.append(n // 2)
    return res
