import re
import itertools
def all_right_truncatable_prime(test_list):
    res = []
    for p in itertools.permutations(test_list, 6):
        tmp = p[:-1]
        while tmp:
            tmp = [int(d) for d in str(p[-1])]
            if all(x%y!=0 for x,y in zip(tmp, p[1:])):
                break
            p = p[:-1]
        else:
            continue
        res.append(p)
    return res
