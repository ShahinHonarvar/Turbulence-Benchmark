def all_right_truncatable_prime(test_tup):
    res = []
    for a in range(test_tup[0] + 1, test_tup[1]):
        if all(a % i != 0 for i in range(2, int(str(a)[-1]))) and a not in res:
            res.append(a)
    return res
