def all_right_truncatable_prime(x):
    res = []
    for i in range(2, int(str(x)[-1]) + 1):
        if all(str(i)[-1] != d for d in range(2, int(str(i)[-1]) + 1)):
            res.append(i)
    return res
