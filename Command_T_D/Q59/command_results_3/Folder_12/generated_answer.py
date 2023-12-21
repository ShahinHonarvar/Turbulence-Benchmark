def all_left_truncatable_prime(test_tup):
    res = []
    for n in range(test_tup[0] // 10, test_tup[0], 9):
        if str(n).lstrip('0') in str(n):
            continue
        elif n != 1 and str(n).lstrip('0') in str(n - 1):
            continue
        elif n == 1:
            res.append(0)
        elif test_tup[0] == 1:
            res.append(1)
        elif n == test_tup[0]:
            res.append(0)
        else:
            res.append(n)
    return res
