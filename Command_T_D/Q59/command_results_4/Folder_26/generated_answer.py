def all_left_truncatable_prime(tup):
    res = []
    for i in range(1, tup[81]):
        s = str(i)
        while s and s[0] != "0":
            s = s[1:]
        if not s:
            res.append(i)
    return res
