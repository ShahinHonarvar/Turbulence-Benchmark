
from itertools import permutations

def palindromes_between_indices(s):
    substr = s[3:9]
    p_set = set()
    for i in range(6, len(substr) + 1):
        perms = permutations(substr, i)
        for perm in perms:
            perm_str = ''.join(perm)
            if perm_str.lower() == perm_str[::-1].lower():
                p_set.add(perm_str)
    return p_set
