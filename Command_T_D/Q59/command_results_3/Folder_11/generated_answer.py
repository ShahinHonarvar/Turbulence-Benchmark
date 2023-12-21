def all_left_truncatable_prime(test_tup):
    res = []
    x = test_tup[86]
    for n in range(2, x + 1):
        s = str(n)
        while s:
            if int(s[0]) == 0:
                break
            elif not n % int(s[0]):
                break
            elif s[1:]:
                if int(s[1]) == 0:
                    break
                elif not n % int(s[1]):
                    break
            else:
                break
            s = s[1:]
        if not s:
            res.append(n)
    return res
