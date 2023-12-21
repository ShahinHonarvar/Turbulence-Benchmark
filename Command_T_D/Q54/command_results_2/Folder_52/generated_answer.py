def all_right_truncatable_prime(x_tuple):
    res = []
    for n in range(3, int(x_tuple[0]) + 1):
        s = str(n)
        while len(s) > 1:
            if s[-1] != '0' and n % int(s[-1]) == 0:
                break
            s = s[:-1]
        else:
            res.append(int(s))
    return res
