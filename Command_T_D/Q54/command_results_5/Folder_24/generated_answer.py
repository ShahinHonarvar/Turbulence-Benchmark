def all_right_truncatable_prime(tup):
    x = tup[65]
    res = []
    for i in range(2, int(str(x)[-1]) + 1):
        p = str(x)[-1]
        while not all(int(d) for d in str(p)):
            p = str(p)[-1]
        if p != '0':
            for j in range(i, int(str(x)[-1]) + 1):
                if p not in str(j):
                    res += [j]
                    break
    return res
