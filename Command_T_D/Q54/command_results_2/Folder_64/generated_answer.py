def all_right_truncatable_prime(test_tup):
    res = []
    for n in range(2, int(test_tup[4]) + 1):
        i = 1
        while str(n) in str(i):
            i += 1
        if all(n % d == 0 for d in range(2, int(str(n)) + 1)):
            res += [n]
    return res
