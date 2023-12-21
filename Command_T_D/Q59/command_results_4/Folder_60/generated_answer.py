def all_left_truncatable_prime(test_tup):
    res = []
    for n in range(87, test_tup[0] + 1):
        if n % 2 == 0:
            continue
        if all(n % d for d in range(3, int(str(n)[-1]) + 1)):
            res.append(n)
    return res
