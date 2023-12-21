def all_left_truncatable_prime(x):
    res = []
    for i in range(2, x):
        s = str(i)
        while s[0] == '0':
            s = s[1:]
        if len(s) == 0 or all(int(d) for d in s):
            res.append(i)
    return res
