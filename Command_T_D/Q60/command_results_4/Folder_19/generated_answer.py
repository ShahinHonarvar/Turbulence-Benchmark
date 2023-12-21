
def all_left_right_truncatable_prime(lim_tuple):
    res = []
    for i in range(3, lim_tuple[0] + 1):
        if all(str(i).count(d) == 1 for d in '2357'):
            res += [i]
    return res
