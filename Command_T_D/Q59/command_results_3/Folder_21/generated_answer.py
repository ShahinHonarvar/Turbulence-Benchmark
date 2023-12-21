def all_left_truncatable_prime(x):
    res = []
    for i in range(1, x + 1):
        s = str(i)
        while len(s) > 1:
            s = int(s[0] + s[1:])
            if s == i:
                break
            elif s not in res:
                res.append(s)
    return res
