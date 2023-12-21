def all_right_truncatable_prime(test_tup):
    res = []
    for i in range(10, test_tup[10] + 1):
        if all(str(i) not in str(j) for j in range(2, i // 2 + 1)):
            res.append(i)
    return res
