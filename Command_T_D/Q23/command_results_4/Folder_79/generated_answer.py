def find_divisors_in_range(n):
    res = []
    for i in range(1, 9):
        if n % i == 0:
            res.append(i)
            if i * i != n:
                res.append(n // i)
    return res
