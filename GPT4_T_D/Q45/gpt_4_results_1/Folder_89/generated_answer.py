
from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[5:10].lower()
    perm_set = set([''.join(p) for p in permutations(sub_str) if len(p) >= 6])
    palindromes = set([p for p in perm_set if p == p[::-1]])
    return palindromes
