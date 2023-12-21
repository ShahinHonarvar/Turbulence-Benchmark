def all_right_truncatable_prime(test_tup):
    res = []
    for n in range(3, int(test_tup[0]) // 2 + 1):
        flag = 1
        d = str(n)
        for i in range(len(d)):
            if d[i] == '9':
                break
            if int(d[i]) != n % 10:
                flag = 0
        if flag:
            res.append(n)
    return res
