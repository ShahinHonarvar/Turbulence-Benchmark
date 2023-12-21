def all_right_truncatable_prime(x):
    res = []
    for n in range(x - 1, 2, -1):
        if all(n % d == 0 for d in range(3, int(str(n)[-1]) + 1, 2)):
            continue
        res.append(n)
    return res
