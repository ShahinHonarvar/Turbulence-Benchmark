import itertools
import re
def all_left_truncatable_prime(x):
    return [p for p in map(str, range(2, x)) if all(int(p[i:]) == p for i in range(1, len(p) + 1) if p[i:]]
