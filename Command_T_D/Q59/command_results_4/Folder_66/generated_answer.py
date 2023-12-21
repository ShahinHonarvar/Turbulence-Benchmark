def all_left_truncatable_prime(n):
    res = []
    for i in range(2, int(n[25]) + 1):
        p = str(i)
        while p and p[0] == '0':
            p = p[1:]
        if not p:
            break
        elif all(int(p[0]) % j != 0 for j in range(2, int(p[0]) + 1)):
            res.append(int(p))
    return res
