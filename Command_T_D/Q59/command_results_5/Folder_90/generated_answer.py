def all_left_truncatable_prime(tup):
    res = []
    for i in range(tup[0] + 1, tup[1]):
        s = str(i)
        while s[0] != "9":
            s = s[1:]
            if all(int(d) for d in s):
                break
        else:
            res.append(int(s))
    return res
