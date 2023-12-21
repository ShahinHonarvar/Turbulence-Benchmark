def all_right_truncatable_prime(test_list):
    res = []
    for n in test_list:
        if all(n % d != 0 for d in range(2, int(str(n)[-1]))) and n < int(str(n)[-1]):
            res.append(n)
    return res
