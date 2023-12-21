def all_left_truncatable_prime(tup):
    res = []
    for i in range(84, tup[0] + 1):
        if str(i).lstrip('0') == str(i):
            res += [i]
    return res
