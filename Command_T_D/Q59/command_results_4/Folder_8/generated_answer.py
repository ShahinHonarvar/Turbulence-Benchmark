def all_left_truncatable_prime(tup):
    res = []
    for i in range(3, int(str(max(tup))[0]) + 1):
        x = str(i)
        while x:
            y = int(x[0])
            if y <= 2:
                break
            if y not in tup:
                res += [y]
            x = x[1:]
    return res
