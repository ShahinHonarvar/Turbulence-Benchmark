import itertools
import re
def all_right_truncatable_prime(test_tup):
    x, = test_tup
    lst = []
    for p in itertools.permutations(str(x)):
        if re.match(r'^[1-9][\d]99', p):
            lst.append(int(p))
    return sorted(lst, reverse=True)
