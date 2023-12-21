def all_right_truncatable_prime(test_list):
    res = []
    for n in test_list:
        for i in range(10):
            if str(n - 1)[:-1] in str(n):
                break
            elif n - 1 in range(2, n // 2):
                res.append(n - 1)
                break
    return res
