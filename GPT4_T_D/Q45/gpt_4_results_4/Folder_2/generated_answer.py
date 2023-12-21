
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:6]
    palindromes = set()

    for i in range(6, len(s)+1):
        perms = permutations(s, i)
        for perm in perms:
            perm_str = ''.join(perm)
            if perm_str.lower() == perm_str[::-1].lower():
                palindromes.add(perm_str)
                
    return palindromes
