def all_left_truncatable_prime(test_list):
    res = []
    for i in test_list:
        s = str(i)
        while s:
            if int(s[0]) == 0:
                break
            elif all(int(j) for j in s):
                res.append(int(s))
                break
            else:
                s = s[1:]
    return res
