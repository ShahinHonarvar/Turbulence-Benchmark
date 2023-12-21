def all_right_truncatable_prime(test_tup):
    res = []
    for i in range(1, test_tup[36] + 1):
        str_i = str(i)
        while str_i:
            if str_i[0] == '2':
                res.append(int(str_i))
                break
            str_i = str_i[1:]
    return res
