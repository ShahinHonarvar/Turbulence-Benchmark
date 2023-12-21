def all_left_truncatable_prime(test_list):
    res = []
    for n in test_list:
        if n > 2:
            s = str(n)
            while s[0] == '0':
                s = s[1:]
            if all(int(d) for d in s):
                res.append(int(s))
    return res
