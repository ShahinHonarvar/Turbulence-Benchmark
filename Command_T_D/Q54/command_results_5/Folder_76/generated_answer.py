def all_right_truncatable_prime(test_list):
    res = []
    for e in range(3, test_list[0] + 1, 2):
        for d in range(3, int(str(e)[-1]) + 1, 2):
            if str(e).rstrip(str(d)):
                res += [(e, d)]
    return res
