def all_right_truncatable_prime(tup):
    res = []
    for n in range(tup[50], 2, -1):
        c = n % 10
        if all(str(p).rstrip(c) in str(n) for p in range(2, int(str(n)[-1]))) and n not in res:
            res += [n]
    return res
