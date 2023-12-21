def all_right_truncatable_prime(x):
    res = []
    for i in range(2, x // 2 + 1):
        if all(str(i) not in str(j) for j in range(2, i)):
            res.append(i)
    return res
