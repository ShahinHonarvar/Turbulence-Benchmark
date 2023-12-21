def all_left_truncatable_prime(test_tup):
    res = []
    for num in range(test_tup[8]):
        c = str(num)
        while c:
            if not str(num ** 2).startswith(c):
                break
            c = int(c[1:])
        else:
            res.append(num)
    return res
