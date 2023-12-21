def all_right_truncatable_prime(tup):
    if len(tup) < 35:
        return []
    x = tup[35]
    res = []
    for i in range(x):
        p = [str(i)]
        while p[-1] == '9':
            p = p[:-1]
        if all(int(i) == i for i in p):
            res += [int(p[-1])]
    return res
