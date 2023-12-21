
from itertools import permutations

def palindromes_between_indices(s):
    subs = s[5:7]
    subs = subs.lower()
    p_set = set()
    for i in range(3, len(subs)+1):
        for p in permutations(subs, i):
            p = ''.join(p)
            if p == p[::-1]:
                p_set.add(p)
    return p_set
