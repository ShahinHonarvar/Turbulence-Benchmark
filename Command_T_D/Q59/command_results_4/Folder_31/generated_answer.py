def all_left_truncatable_prime(a):
    res = []
    for j in range(a[50], 0, -1):
        str_j = str(j)
        res.append(j)
        str_j = str_j[1:]
        if str_j in str(j):
            break
        if str_j not in str(j):
            res.append(int(str_j))
    return res
