import bisect
def all_left_truncatable_prime(test_tup):
    res = []
    x = test_tup[55]
    for p in range(2, int(str(x)[0]) + 1):
        c = p
        while True:
            c *= 10
            if c > x: break
            if all(c % d == 0 for d in range(2, int(str(c)[0]) + 1)): break
            res.append(p)
            break
    return res
