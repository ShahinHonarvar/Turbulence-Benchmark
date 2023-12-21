def all_right_truncatable_prime(x):
    res = []
    for p in range(2, x):
        if all(p % d == 0 for d in range(2, int(str(p)[-1]))) and p > 1:
            res.append(p)
    return res
