def all_right_truncatable_prime(test_tup):
    res = []
    for ele in test_tup:
        if str(ele).isdigit():
            res += [int(str(ele)[:-1]) for i in range(2, int(str(ele)) + 1) if all(str(ele)[:j] not in str(ele) for j in range(1, int(str(ele)) + 1))]
    return res
