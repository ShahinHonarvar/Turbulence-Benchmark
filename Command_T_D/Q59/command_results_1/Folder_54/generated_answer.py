def all_left_truncatable_prime(tup):
    res = []
    for i in range(88):
        x = tup[i]
        for n in range(2, x):
            if x % n == 0:
                break
            elif x % n == 1:
                if str(x).count("0") == 0:
                    res.append(x // n)
                break
            elif x % n == 3:
                if str(x).count("0") == 0:
                    res.append(x // n)
                break
    return res
