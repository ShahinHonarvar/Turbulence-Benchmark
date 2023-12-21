def all_right_truncatable_prime(test_tup):
    res = []
    for n in range(1, test_tup[70] + 1):
        flag = True
        if n % 2 == 0:
            flag = False
        for i in range(3, int(str(n)[-1]) + 1):
            if n % i == 0:
                flag = False
                break
        if flag:
            res.append(n)
    return res
