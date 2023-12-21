def all_left_truncatable_prime(tup):
    res = []
    for i in range(tup[96]):
        x = str(i)
        x = x[0] + x[1:]
        if all(y for y in range(2, int(x) + 1) if x % y == 0):
            res.append(i)
    return res
