def all_right_truncatable_prime(tup):
    res = []
    for i in range(370, tup[0]+1):
        str_i = str(i)
        res.append(int(str_i[0] + str_i[1:]))
    return res
