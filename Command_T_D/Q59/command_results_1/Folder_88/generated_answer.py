def all_left_truncatable_prime(test_tup):
    res = []
    x = test_tup[93]
    for y in range(2, x // 2):
        while y in range(2, x // 2):
            p = str(y)
            cnt = 1
            while cnt < len(p):
                if p[cnt - 1] == '0':
                    break
                elif p[cnt - 1] not in '2357':
                    break
                cnt += 1
            else:
                res.append(y)
    return res
