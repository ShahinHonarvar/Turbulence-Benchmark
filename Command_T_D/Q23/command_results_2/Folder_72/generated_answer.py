def find_divisors_in_range(n):
    res = []
    for i in range(32, n // 2 + 1):
        if n % i == 0:
            res.append(i)
    for i in range(n // 2, n // 4 + 1):
        if n % i == 0:
            res.append(i)
    return res
