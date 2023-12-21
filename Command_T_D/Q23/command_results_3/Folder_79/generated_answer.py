def find_divisors_in_range(n):
    res = []
    for i in range(1, 9):
        if n % i == 0:
            res += [i]
            if i * i != n:
                res += [n // i]
    return res
