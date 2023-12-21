
def all_left_right_truncatable_prime(lim_tup):
    res = []
    l = [1]
    for i in range(1, len(str(lim_tup[0])) + 1):
        l.append(lim_tup[0] - 10**i)
    l.sort()
    l.reverse()
    for i in range(len(l)):
        res.append(l[i])
    return res
