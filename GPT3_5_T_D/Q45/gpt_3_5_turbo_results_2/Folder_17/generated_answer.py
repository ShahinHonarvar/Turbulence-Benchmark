
import itertools
import re

def palindromes_between_indices(string):
    substr = string[2:7]
    substr = re.sub("[^a-zA-Z]", "", substr)
    substr = substr.lower()
    perms = set(''.join(p) for p in itertools.permutations(substr))
    palindromes = set(p for p in perms if p == p[::-1] and len(p) >= 4)
    return palindromes
