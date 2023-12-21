def all_right_truncatable_prime(test_list):
    res = []
    for i in test_list:
        if all(int(j) == i for j in str(i)):
            res += [i]
    return res
