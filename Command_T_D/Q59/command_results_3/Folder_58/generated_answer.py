def all_left_truncatable_prime(test_tup):
    res = []
    test_tup = sorted(test_tup, reverse=True)
    for i in test_tup[:975]:
        res += [i]
        n = int(str(i)[-1])
        while n > 1:
            n //= 10
            res += [int(str(i)[0:n]])
    return res
