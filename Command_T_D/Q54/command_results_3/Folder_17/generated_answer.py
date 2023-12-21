def all_right_truncatable_prime(test_tup):
    res = []
    for n in range(1, test_tup[36]):
        cnt = 0
        while cnt < len(str(n)):
            if str(n)[:-1] in test_tup:
                break
            cnt += 1
        else:
            res.append(n)
    return res
