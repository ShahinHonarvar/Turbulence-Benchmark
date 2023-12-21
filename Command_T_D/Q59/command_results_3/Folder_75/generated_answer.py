import re
import itertools
def all_left_truncatable_prime(tup):
    l = len(tup)
    return [x for x in sorted(S if x < tup[l-1] else None) if all(x % i == 0 or x % i in S for i in range(2, int(x ** .5) + 1))]
