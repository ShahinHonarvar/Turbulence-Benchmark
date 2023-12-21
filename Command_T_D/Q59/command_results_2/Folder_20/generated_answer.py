def all_left_truncatable_prime(tup):
    res = []
    for x in range(tup[100], 1, -1):
        if x == 1:
            break
        s = str(x)
        while s[0] == '0':
            s = s[1:]
        if len(s) == 0:
            break
        if all(int(s[i]) % 10 == 0 for i in range(1, len(s))):
            break
        elif all(int(s[i]) * 10 + int(s[i + 1]) <= x for i in range(1, len(s) - 1)):
            res.append(x)
    return res
