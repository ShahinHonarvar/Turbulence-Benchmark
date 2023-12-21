def all_right_truncatable_prime(test_tup):
    res = []
    for a in range(3, test_tup[4]):
        b = a
        c = a
        while b % 2 == 0:
            b /= 2
        while b != 1 and b not in res:
            res += [b]
            c *= 10
            while c not in res:
                res += [c]
                c *= 10
    return res
