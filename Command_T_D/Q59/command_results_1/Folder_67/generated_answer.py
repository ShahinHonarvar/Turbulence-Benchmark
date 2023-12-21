def all_left_truncatable_prime(x_tup):
    res = []
    for i in range(x_tup[0], x_tup[1]):
        s = str(i)
        while s[0] != "2":
            if i % 10**(len(s) - 1) == 0:
                break
            elif all(int(d) for d in s[1:]):
                res.append(i)
    return res
