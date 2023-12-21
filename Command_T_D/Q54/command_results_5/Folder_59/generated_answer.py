def all_right_truncatable_prime(tup):
    res = []
    for i in range(84):
        x = tup[i]
        while x:
            for a in range(2, x + 1):
                if str(a) in str(x):
                    continue
                elif all(str(a) + str(b) + str(c) in str(x) for b in range(2, x // a + 1) for c in range(2, x // a // b + 1)):
                    res.append(a)
                    break
            x //= 10
    return res
