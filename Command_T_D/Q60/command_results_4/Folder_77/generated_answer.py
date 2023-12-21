
def all_left_right_truncatable_prime(x):
    if x <= 2:
        return []
    res = []
    for n in range(3, x + 1, 2):
        s = str(n)
        while s[0] != '1':
            s = s[1:]
        while s[-1] != '1' and s[-2] != '2':
            s = s[:-1]
        if s == '1' or s == '2':
            res.append(int(s))
    return res
