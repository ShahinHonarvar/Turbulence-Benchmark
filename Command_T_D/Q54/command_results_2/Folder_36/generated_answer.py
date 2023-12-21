def all_right_truncatable_prime(lst):
    res = []
    for x in range(1, lst[992] + 1):
        for y in range(x, lst[992] + 1, x):
            if all(int(d) == d for d in str(y)):
                res.append(y)
                break
    return res
