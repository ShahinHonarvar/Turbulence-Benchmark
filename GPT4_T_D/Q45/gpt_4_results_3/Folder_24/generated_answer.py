
from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:10]
    if len(s) < 4:
        return set()
    else:
        res = set()
        for i in range(4, len(s) + 1):
            perms = [''.join(p) for p in permutations(s, i)]
            for perm in perms:
                if perm.lower() == perm[::-1].lower():
                    res.add(perm)
        return res
