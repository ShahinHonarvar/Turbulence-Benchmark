
from itertools import permutations

def palindromes_between_indices(s):
    s = s[6:9].lower()
    res = set()
    for i in range(3, len(s) + 1):
        for permut in permutations(s, i):
            cand = ''.join(permut)
            if cand == cand[::-1]:
                res.add(cand)
    return res
