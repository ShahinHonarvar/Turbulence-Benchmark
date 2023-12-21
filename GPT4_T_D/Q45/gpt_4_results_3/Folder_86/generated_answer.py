
from itertools import permutations

def palindromes_between_indices(s):
    substr = s[6:10].lower()
    pals = set()
    for i in range(4, len(substr)+1):
        perms = permutations(substr,i)
        for perm in perms:
            perm_s = ''.join(perm)
            if perm_s == perm_s[::-1]:
                pals.add(perm_s)
    return pals
