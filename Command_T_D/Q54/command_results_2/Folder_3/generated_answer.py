def all_right_truncatable_prime(tup):
    res = []
    for x in range(tup[100], 2, -1):
        for i in range(10):
            tmp = str(x)
            while not str(x // 10**i).isalnum():
                tmp = tmp[:-1]
            if all(int(d) for d in tmp):
                res.append(x)
    return res
