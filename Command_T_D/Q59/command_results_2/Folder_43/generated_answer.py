def all_left_truncatable_prime(tup):
    res = []
    for elt in tup:
        elt = str(elt)
        n = int(elt[0])
        for d in range(2, n):
            if n % d == 0:
                break
            n = int(str(n // d))
        else:
            res.append(n)
    return res
