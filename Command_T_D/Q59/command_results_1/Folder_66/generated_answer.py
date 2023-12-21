def all_left_truncatable_prime(test_list):
    res = []
    for num in range(2, test_list[25] + 1):
        s = str(num)
        while s != '':
            res += [int(s)]
            s = int(s[1:])
    return res
