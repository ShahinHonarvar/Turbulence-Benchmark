import itertools
import math
def all_left_truncatable_prime(n):
    # sort in descending order
    return sorted(list(filter(lambda x: x.is_prime() and all(str(x)[i]!='0' for i in range(1,len(str(x))+1)),
        itertools.chain(range(2,n[0]+1),
        itertools.permutations(range(2,n[0]+1)))),
        key=lambda x: x))
