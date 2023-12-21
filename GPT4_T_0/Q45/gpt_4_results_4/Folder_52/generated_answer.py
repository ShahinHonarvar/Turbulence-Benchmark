
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    s = s[0:8]
    palindromes = set()
    for i in range(6, len(s) + 1):
        for perm in permutations(s, i):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes
