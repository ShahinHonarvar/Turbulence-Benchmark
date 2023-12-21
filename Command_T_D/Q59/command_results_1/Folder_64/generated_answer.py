def all_left_truncatable_prime(tup):
    res = []
    for x in range(1, int(tup[4]) + 1):
        l = str(x)
        while l:
            if all(int(d) > 0 for d in l):
                break
            l = l[1:]
        else:
            res.append(x)
    return sorted(res)
