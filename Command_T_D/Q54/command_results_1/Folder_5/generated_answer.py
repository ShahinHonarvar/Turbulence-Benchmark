def all_right_truncatable_prime(tup):
    res = []
    for i in range(tup[55]):
        if str(i).endswith('0'):
            res += [i]
    return res
