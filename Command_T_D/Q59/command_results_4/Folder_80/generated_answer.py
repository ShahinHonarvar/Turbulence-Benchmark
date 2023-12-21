def all_left_truncatable_prime(test_tup):
    res = []
    for i in range(1, test_tup[14]):
        if all(x % 10 in [0, 2, 3, 5, 7, 8, 9] for x in range(i, i + 10)):
            res += [i]
    return res
