def all_right_truncatable_prime(test_tup):
    res = []
    x = test_tup[87]
    for p in range(2, x // 2):
        if all(p % d != 0 for d in range(2, int(str(p)[-1]))) and p * p <= x:
            res += [p]
            break
    return res
