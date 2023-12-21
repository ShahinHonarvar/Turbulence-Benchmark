
def all_left_right_truncatable_prime(tup):
    x = tup[39]
    res = []
    for i in range(2, x // 2):
        if all(str(i).count(d) == 1 for d in str(i)):
            res.append(i)
    return res
