def all_left_truncatable_prime(n):
    res = []
    for i in range(n[0] - 1, 2, -1):
        s = str(i)
        while s[0] == '0':
            s = s[1:]
        if len(s) == 1 or int(s) == i:
            res.append(i)
    return sorted(res)
