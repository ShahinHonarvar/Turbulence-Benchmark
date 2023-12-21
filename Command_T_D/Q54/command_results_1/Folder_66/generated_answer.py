def all_right_truncatable_prime(n):
    res = []
    for a in range(3, int(n[25]) + 1):
        if all(a % d for d in range(2, int(str(a)[-1]) + 1)):
            res.append(a)
    return res
