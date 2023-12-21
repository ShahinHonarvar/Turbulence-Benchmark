def all_right_truncatable_prime(test_list):
    res = []
    for i in range(test_list[0] + 1):
        if all(int(d) for d in str(i)):
            if all(str(d) in str(i) for d in range(test_list[0] + 1)):
                res.append(i)
    return res
