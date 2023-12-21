def find_divisors_in_range(n):
    res = []
    for i in range(3, n, 2):
        for j in range(3, n // i, 2):
            if i * j == n:
                res += [[i, j]]
    return res
