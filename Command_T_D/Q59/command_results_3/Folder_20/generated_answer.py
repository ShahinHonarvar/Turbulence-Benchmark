def all_left_truncatable_prime(tup):
    res = []
    for i in range(100, tup[0] + 1):
        temp = str(i)
        while temp:
            if all(int(d) > 0 for d in temp):
                break
            temp = int(temp[1:])
        else:
            res.append(i)
    return res
