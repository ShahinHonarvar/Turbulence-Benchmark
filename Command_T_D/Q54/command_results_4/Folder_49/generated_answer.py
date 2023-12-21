def all_right_truncatable_prime(x):
    res = []
    for i in range(2, x // 2):
        res += [i]
        if str(i) in str(x):
            break
    return res
