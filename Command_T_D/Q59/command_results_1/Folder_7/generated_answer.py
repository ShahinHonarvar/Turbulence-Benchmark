def all_left_truncatable_prime(tup):
    res = []
    for i in range(1, tup[0] + 1):
        s = str(i)
        while s[0] == '0':
            s = s[1:]
        if all(x == '0' or str(x) in s for x in range(10)):
            res.append(i)
    return res
