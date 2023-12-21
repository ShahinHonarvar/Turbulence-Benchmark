def all_right_truncatable_prime(test_list):
    res = []
    for t in test_list:
        x = t[67]
        while x > 1:
            x //= 10
            if x == 1:
                res.append(t)
                break
    return res
