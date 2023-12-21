def all_right_truncatable_prime(test_list):
    res = []
    for n in range(test_list[46] - 1, 2, -1):
        if all(n % d for d in range(3, int(str(n)[-1]) + 1, 2)):
            res.append(n)
    return res
