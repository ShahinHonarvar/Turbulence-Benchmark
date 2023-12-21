def all_left_truncatable_prime(n):
    res = []
    for i in range(2, int(n[33]) + 1):
        while str(i)[:-1] in res:
            i += 1
        if i not in res:
            res.append(i)
    return sorted(res)
