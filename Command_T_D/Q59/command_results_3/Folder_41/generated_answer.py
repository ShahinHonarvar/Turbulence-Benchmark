def all_left_truncatable_prime(test_tup):
    res = []
    for i in range(2, int(test_tup[46]) + 1):
        if all(str(i).count(c) == 1 for c in str(i)):
            res.append(i)
    return res
