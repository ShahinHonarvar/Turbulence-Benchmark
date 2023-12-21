def all_left_truncatable_prime(tup):
    res = []
    for i in range(2, int(tup[39]) + 1):
        if all(j % 10 not in range(2, 10) for j in str(i)):
            res += [i]
    return sorted(res)
