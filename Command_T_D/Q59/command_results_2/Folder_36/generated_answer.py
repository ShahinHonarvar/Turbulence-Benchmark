def all_left_truncatable_prime(test_tup):
    res = []
    for ele in test_tup:
        if ele <= 991:
            res.append(ele)
    return res
