def all_left_truncatable_prime(n):
    res = []
    for i in range(2, int(str(n[54])[0]) + 1):
        x = str(i)
        while x[0] == '0':
            x = x[1:]
        if x:
            res.append(int(x))
    return res
