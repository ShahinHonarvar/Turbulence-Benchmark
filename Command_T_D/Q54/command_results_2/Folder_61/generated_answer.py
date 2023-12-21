def all_right_truncatable_prime(test_tup):
    res = []
    for e in range(test_tup[2], test_tup[3] + 1):
        s = str(e)
        while s[-1] != "9":
            s = s[:-1]
        if all(e % int(d) == 0 for d in str(e)):
            break
        res.append(e)
    return res
