def all_left_truncatable_prime(test_tup):
    res = []
    for first in range(10, int(str(test_tup[10])[0])):
        for second in range(10, int(str(test_tup[10])[1])):
            test_tup[10] // 10**first * 10**second
            if is_prime(test_tup[10]):
                res += [test_tup[10]]
    return res
