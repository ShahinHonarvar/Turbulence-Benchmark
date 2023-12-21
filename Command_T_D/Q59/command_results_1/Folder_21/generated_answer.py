def all_left_truncatable_prime(tup):
    res = []
    for n in range(tup[0] + 1):
        s = str(n)
        while len(s) > 1:
            s = s[1:]
            if all(int(i) for i in s):
                break
            else:
                res.append(n)
    return res
