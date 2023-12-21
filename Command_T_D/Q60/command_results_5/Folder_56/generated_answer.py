
def all_left_right_truncatable_prime(lim_n):
    res = []
    for i in range(2, int(str(lim_n[0])[0]) + 1):
        if all(str(i).count(d) == 1 for d in str(i)):
            res += [i]
    return res
