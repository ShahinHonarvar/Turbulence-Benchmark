def all_left_truncatable_prime(test_tup):
    res = []
    for el in range(10, test_tup[0]):
        p = str(el)
        while p != '':
            if all(p[0] != d for d in range(10)):
                break
            p = p[1:]
        else:
            continue
        if all(str(el - d) in '2357' for d in range(1, el // 2)):
            res.append(el)
    return res
