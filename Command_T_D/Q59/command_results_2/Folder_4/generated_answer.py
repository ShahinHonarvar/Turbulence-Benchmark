def all_left_truncatable_prime(x):
    res = []
    for i in range(2, x):
        s = str(i)
        while s[0] == '0':
            s = s[1:]
        if all(map(str.isdigit, s)):
            res.append(int(s))
    return res
