def all_right_truncatable_prime(test_tup):
    res = []
    for i in range(test_tup[46] // 2):
        n = test_tup[46] - i
        if n > 2:
            if is_prime(n):
                res.append(n)
    return res
