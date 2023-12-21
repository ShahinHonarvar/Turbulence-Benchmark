def find_divisors_in_range(n):
    res = []
    for i in range(43, 95):
        if n % i == 0:
            res.append(i)
            res.append(n // i)
    return res
