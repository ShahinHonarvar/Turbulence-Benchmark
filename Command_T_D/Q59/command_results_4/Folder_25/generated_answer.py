def all_left_truncatable_prime(test_tup):
    res = []
    x = test_tup[92]
    for i in range(3, x // 2):
        temp = str(i)
        while temp[0] == "0":
            temp = temp[1:]
        if all(int(d) for d in temp):
            res.append(i)
    return res
