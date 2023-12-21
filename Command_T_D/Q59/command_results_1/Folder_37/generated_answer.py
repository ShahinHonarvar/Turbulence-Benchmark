def all_left_truncatable_prime(tup):
    res = []
    for i in range(1, tup[35] + 1):
        s = str(i)
        while s[0] != "9":
            s = int(s[1:])
            if s == i and all(str(x).isdigit() for x in range(2, s)):
                res.append(i)
    return res
