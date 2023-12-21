def all_left_truncatable_prime(test_case):
    test_case = list(test_case)
    test_case.sort()
    res = []
    for t in test_case:
        if t > 2:
            p = str(t)
            while p != '':
                if p[0] == '0':
                    break
                elif int(p[0]) * 10**(len(p) - 1) == t:
                    break
                else:
                    p = int(p[1:])
            else:
                res.append(t)
    return res
