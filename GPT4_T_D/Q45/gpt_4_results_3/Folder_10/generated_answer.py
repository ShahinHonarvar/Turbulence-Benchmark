
from itertools import permutations
def palindromes_between_indices(s):
    s = s[0:6].lower()
    pals = set()
    for i in range(3, len(s) + 1):
        perms = permutations(s, i)
        for p in perms:
            possible_pal = ''.join(p)
            if possible_pal == possible_pal[::-1]:
                pals.add(possible_pal)
    return pals
