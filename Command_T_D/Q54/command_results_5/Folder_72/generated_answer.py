def all_right_truncatable_prime(n):
    res = []
    for x in range(n[0], n[1] + 1):
        if all(x % d for d in range(2, int(str(x)[-1]) + 1)):
            res.append(x)
    return res
