
import itertools

def all_left_right_truncatable_prime(n):
    res = []
    for p in itertools.permutations(list(str(n)), 2):
        tmp = p[0] + p[1]
        if int(tmp) <= n and tmp[0] == '2' and tmp[1] == '5' and tmp[2:] in str(n):
            res += [int(tmp)]
    return res
