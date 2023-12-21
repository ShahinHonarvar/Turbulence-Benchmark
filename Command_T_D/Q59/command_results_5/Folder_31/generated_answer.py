def all_left_truncatable_prime(tup):
    res = []
    for e in range(2, tup[50] + 1):
        if e in tup and all(e % d == 0 for d in range(3, int(str(e).lstrip('0')) + 1)):
            res.append(e)
    return res
