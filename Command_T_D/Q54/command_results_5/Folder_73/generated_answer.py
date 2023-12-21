def all_right_truncatable_prime(tup):
    res = []
    for i in range(len(tup[97]) - 1):
        tmp = tup[97]
        for j in range(i, len(tmp)):
            tmp //= 10**j
        if all(tmp % d for d in range(2, tmp // 2 + 1)):
            res.append(tmp)
    return res
