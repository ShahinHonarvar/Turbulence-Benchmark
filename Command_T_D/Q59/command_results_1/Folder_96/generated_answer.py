def all_left_truncatable_prime(test_tup):
    res = []
    x = test_tup[29]
    for i in range(2, x // 2):
        s = str(i)
        if s[0] != '0' and all(s[0] != c for c in s[1:]):
            res.append(i)
    return res
