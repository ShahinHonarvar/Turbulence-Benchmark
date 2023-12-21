def find_divisors_in_range(n):
    res = []
    for i in range(33, 57 + 1):
        if n % i == 0:
            res += [i]
    return res
