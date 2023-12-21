
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    substr = s[0:7]
    palindromes = set()
    for i in range(7, len(substr) + 1):
        perms = permutations(substr, i)
        for perm in perms:
            str_ = ''.join(perm)
            if str_ == str_[::-1]:
                palindromes.add(str_)
    return palindromes
