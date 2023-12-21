def all_right_truncatable_prime(test_tup):
    res = []
    for a in range(test_tup[23] // 2, test_tup[23], -1):
        while True:
            tmp = str(a)
            if len(tmp) == 1:
                break
            elif tmp[-1] in "02468":
                break
            else:
                a += 1
    return res
