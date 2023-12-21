def all_left_truncatable_prime(test_list):
    res = []
    for i in test_list:
        if i == 0:
            continue
        if i == 1:
            res.append(i)
            continue
        x = list(str(i))
        x.reverse()
        while x:
            if len(x) == 1:
                res.append(int("".join(x)))
                break
            elif x[0] == "0":
                break
            elif not all(str(int(x[0]) + int(w)) for w in x[1:]):
                break
            else:
                res.append(int("".join(x)))
    return res
