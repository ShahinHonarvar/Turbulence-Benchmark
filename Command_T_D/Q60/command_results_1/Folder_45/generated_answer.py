
def all_left_right_truncatable_prime(tup):
    x = tup[61]
    res = []
    for p in range(2, x // 2 + 1):
        s = str(p)
        while s[0] != '0':
            s = s[1:]
        if s[0] == '0':
            continue
        while s[-1] != '0':
            s = s[:-1]
        if s[-1] == '0':
            continue
        if p == int(s):
            continue
        if p == int(s[0] + s[1:]):
            continue
        if p == int(s[-2] + s[-1]):
            continue
        if p == int(s[0] + s[1:-2] + s[-2] + s[-1]):
            continue
        res.append(p)
    return sorted(res)
