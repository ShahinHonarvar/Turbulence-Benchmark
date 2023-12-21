def all_right_truncatable_prime(tup):
    res = []
    for n in range(10, int(tup[11]) + 1):
        if n in tup[0]:
            continue
        elif str(n) in tup[1]:
            continue
        elif all(n % d == 0 for d in range(3, int(str(n)[-1]) + 1, 2)):
            continue
        elif all(n % d != 0 for d in range(3, int(str(n)[-1]) + 1, 2)):
            res.append(n)
    return res
