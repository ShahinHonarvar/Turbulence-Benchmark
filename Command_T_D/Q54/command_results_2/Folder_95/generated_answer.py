def all_right_truncatable_prime(test_tup):
    res = []
    for e in range(2, test_tup[77] + 1):
        if all(e % d == 0 for d in range(3, int(e ** .5) + 1)):
            res.append(e)
    return res
