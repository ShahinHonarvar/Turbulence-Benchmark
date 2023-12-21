def all_left_truncatable_prime(test_tup):
    res = []
    for n in range(2, test_tup[43] + 1):
        if all(str(n).count(d) == 1 for d in str(n)):
            if n not in res:
                res.append(n)
    return sorted(res)
