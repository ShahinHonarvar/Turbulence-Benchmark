def all_right_truncatable_prime(test_list):
    res = []
    for n in range(2, int(test_list[81])+1):
        while str(n) in test_list:
            n += 1
        if all(n % d == 0 for d in range(2, int(str(n))+1)):
            res.append(n)
    return res
