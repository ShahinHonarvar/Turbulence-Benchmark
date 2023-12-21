
def all_left_right_truncatable_prime(test_case):
    res = []
    for p in range(test_case[0], test_case[1] + 1):
        for i in range(2, p // 2 + 1):
            if str(p).count(str(i)) == 2:
                res.append(p)
    return res
