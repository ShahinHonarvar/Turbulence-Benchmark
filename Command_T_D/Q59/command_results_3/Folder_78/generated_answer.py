def all_left_truncatable_prime(tup):
    res = []
    for a in range(1, tup[23]):
        s = str(a)
        while s and s[0] == '0':
            s = s[1:]
        if not s:
            continue
        for i in range(1, len(s)):
            b = int(s[:i])
            if b * b <= a:
                break
            if all(b % d == 0 for d in range(2, int(s[i:]))) and b > 1:
                break
        else:
            res.append(a)
    return res
