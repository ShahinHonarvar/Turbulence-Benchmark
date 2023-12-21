def all_left_truncatable_prime(x):
    res = []
    for i in range(2, x // 2):
        res += [str(i)]
        for j in range(i + 1, x // 2):
            if str(j) not in res:
                res += [str(j)]
                break
    return sorted(set(res))
