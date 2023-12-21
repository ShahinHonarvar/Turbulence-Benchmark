def all_left_truncatable_prime(x):
    res = []
    for i in range(2, x // 2):
        s = str(i)
        while s[0] == '0':
            s = s[1:]
        if s == '':
            continue
        elif all(int(s[0]) % j == 0 for j in range(2, int(s[0]) + 1)):
            continue
        elif all(str(i) == s or int(s[0]) % j == 0 for j in range(2, int(s[0]) + 1)):
            continue
        else:
            res.append(i)
    return sorted(res)
