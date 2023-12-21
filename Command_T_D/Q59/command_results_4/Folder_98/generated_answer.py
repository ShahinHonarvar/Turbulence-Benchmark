def all_left_truncatable_prime(test_tup):
    res = []
    for ele in range(test_tup[0], test_tup[1] + 1):
        while str(ele).rstrip("0") in str(ele).rstrip("0") + str(ele)[1:]:
            ele += 1
        if is_prime(ele):
            res.append(ele)
    return res
