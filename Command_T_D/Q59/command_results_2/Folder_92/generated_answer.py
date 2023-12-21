def all_left_truncatable_prime(test_tup):
    res = []
    for x in range(test_tup[7]):
        for i in range(10):
            if str(x)[:i] == '9' * i:
                continue
            elif str(x)[-1] == '9':
                res += [int(str(x)[:-1])]
            elif str(x) == '9':
                res += [int(str(x)[:-1])]
            else:
                res += [int(str(x)[:-1])]
    return res
