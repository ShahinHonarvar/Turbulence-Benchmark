def all_right_truncatable_prime(test_list):
    res = []
    for n in test_list:
        for i in range(1, int(str(n)[-1]) + 1):
            if str(n)[-1] != str(n - i) and str(n - i) in str(n)[-1]:
                res.append(n - i)
    return res
