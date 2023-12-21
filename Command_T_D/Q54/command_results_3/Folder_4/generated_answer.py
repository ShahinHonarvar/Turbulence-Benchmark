def all_right_truncatable_prime(test_tup):
    res = []
    for e in range(test_tup[96], 2, -1):
        if e % 2 == 0:
            continue
        if all(int(e) % 10**i == 0 for i in range(1, int(math.log10(e)) + 1)):
            res.append(e)
    return res
