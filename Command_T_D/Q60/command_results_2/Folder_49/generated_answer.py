
import itertools

def all_left_right_truncatable_prime(lim):
    l = list(itertools.permutations(str(lim)))
    l.sort()
    if len(l) == 0:
        return []
    l = list(filter(lambda x: x[0] == '1' or x[0] == '2' and x[1] == '2', l))
    l = list(filter(lambda x: x[-1] == '1' or x[-1] == '2' and x[0] == '2', l))
    return list(map(lambda x: int(x[1:-1]), l))
