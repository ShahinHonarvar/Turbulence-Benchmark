def all_right_truncatable_prime(test_tup):
    res = []
    x = test_tup[91]
    for i in range(2, x // 2 + 1):
        if all(int(d) for d in str(i)):
            res += [i]
    return res
