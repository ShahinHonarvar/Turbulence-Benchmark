
from itertools import combinations

def palindromes_between_indices(st):
    substr = st[6:10].lower()
    substr = ''.join(sorted([ch for ch in substr if ch.isalpha()]))
    res = set()
    for l in range(3, len(substr) + 1):
        comb = combinations(substr, l)
        for c in comb:
            c = ''.join(c)
            if c == c[::-1]:
                res.add(c)
    return res
