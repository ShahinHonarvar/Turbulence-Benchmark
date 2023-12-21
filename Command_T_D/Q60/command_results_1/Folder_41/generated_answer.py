
def all_left_right_truncatable_prime(test_tup):
    res = []
    for n in range(test_tup[0] // 2, test_tup[0], 2):
        p = str(n)
        if p[0] != "0" and p[-1] != "0" and p[0] != "1" and p[-1] != "1":
            if int(p[0]) > int(p[1]):
                res.append(n)
            elif int(p[-1]) > int(p[-2]):
                res.append(n)
    return res
