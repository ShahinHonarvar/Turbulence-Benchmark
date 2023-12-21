def all_right_truncatable_prime(n):
    res = []
    for i in range(2, n[8]):
        j = str(i)
        while j and j[0] == '9':
            j = int(j[1:])
        if j == i and i == i ** 2:
            res.append(i)
    return res
