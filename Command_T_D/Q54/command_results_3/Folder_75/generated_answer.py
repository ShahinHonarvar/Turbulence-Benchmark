def all_right_truncatable_prime(test_tup):
    res = []
    for n in range(1, test_tup[41]):
        flag = True
        for d in str(n):
            if n % int(d) == 0:
                flag = False
                break
        if flag:
            res += [n]
    return res
