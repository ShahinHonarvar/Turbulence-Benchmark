def all_right_truncatable_prime(test_list):
    res = []
    for n in range(test_list[0] // 2, test_list[0] // 2 - 1, -1):
        if all(str(n)[-1] != d for d in range(str(n)[-1] + 1)):
            res.append(n)
    return res
