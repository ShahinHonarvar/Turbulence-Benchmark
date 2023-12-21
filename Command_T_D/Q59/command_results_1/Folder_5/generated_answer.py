def all_left_truncatable_prime(num_list):
    res = []
    for n in range(num_list[0], num_list[1]):
        s = str(n)
        while s[0] == '0':
            s = s[1:]
        if len(s) == 0 or all(int(d) for d in s):
            res.append(n)
    return res
