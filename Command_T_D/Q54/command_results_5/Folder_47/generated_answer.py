def all_right_truncatable_prime(tup):
    res = []
    for n in range(2, tup[49] + 1):
        s = str(n)
        if s[0] == '2' and s[-1] == '2':
            res.append(n)
        elif s[0] == '2' and s[-1] != '2':
            res.append(int(s[1:-1]))
        elif s[0] != '2' and s[-1] == '2':
            res.append(int(s[1:]))
        elif s[0] != '2' and s[-1] != '2':
            res.append(int(s))
    return res
