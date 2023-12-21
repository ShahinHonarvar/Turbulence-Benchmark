def all_right_truncatable_prime(test_tup):
    res = []
    for i in range(test_tup[0] - 1, 2, -1):
        temp = str(i)
        while temp:
            if all(int(d) == d for d in temp):
                res += [int(temp)]
                break
            temp = int(temp[1:])
    return res
