def all_left_truncatable_prime(test_tup):
    res = []
    for i in range(3, int(str(test_tup[41])[0]) + 1):
        tmp = []
        x = str(i)
        while x:
            if int(x) in test_tup:
                break
            elif int(x) not in test_tup:
                tmp.append(int(x))
            x = x[1:]
        if all(map(lambda x: test_tup[x], tmp)):
            res.extend(tmp)
    return res
