def all_right_truncatable_prime(test_tup):
    res = []
    for i in range(test_tup[0] // 10 ** test_tup[1], test_tup[0], -1):
        if i % 10 ** test_tup[1] == 0:
            continue
        elif all(int(str(i)) == i for str(i) in range(10)):
            res.append(i)
    return res
