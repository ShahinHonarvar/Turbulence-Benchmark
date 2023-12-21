def all_left_truncatable_prime(x_tuple):
    res = []
    for n in range(x_tuple[0], x_tuple[1]):
        s = str(n)
        while s[0] == '0':
            s = s[1:]
        if all(int(s[i]) for i in range(1, len(s))):
            res.append(int(s))
    return res
