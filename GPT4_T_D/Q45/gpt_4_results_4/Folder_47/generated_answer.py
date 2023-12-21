
from itertools import permutations

def palindromes_between_indices(s):
    subset = s[3:8].lower()
    palindromes = set()
    for i in range(5, len(subset) + 1):
        perms = permutations(subset, i)
        for perm in perms:
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
