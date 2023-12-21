def all_right_truncatable_prime(test_tup):
    res = []
    for n in range(2, test_tup[0] // 2):
        s = str(n)
        while len(s) > 1:
            if int(s[0] + s[1:]) == n:
                break
            s = s[1:]
        else:
            res.append(n)
    return res
