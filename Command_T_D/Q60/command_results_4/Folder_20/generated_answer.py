
import itertools

def all_left_right_truncatable_prime(tup):
    res = []
    for x in tup:
        for p in itertools.permutations(str(x)):
            if str(x)[:len(p) - 1] + str(x)[-len(p) - 1:] == '1':
                res.append(int(p))
        if len(res) > 0:
            break
    return res
