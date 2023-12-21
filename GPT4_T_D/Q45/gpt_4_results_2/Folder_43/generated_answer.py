
from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:6].lower()
    unique_perms = set(''.join(p) for p in permutations(s) if len(''.join(p)) >= 4)
    palindromes = set(word for word in unique_perms if word == word[::-1])
    return palindromes
