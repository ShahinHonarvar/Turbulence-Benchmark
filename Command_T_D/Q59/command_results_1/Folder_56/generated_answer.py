def all_left_truncatable_prime(test_tup):
    res = []
    for i in range(2, test_tup[0]):
        p = [i]
        while p:
            n = int("".join(str(x) for x in p))
            if all(n % x for x in range(3, int(str(n)[-1]))) and n not in res:
                res.append(n)
            p = []
    return res
