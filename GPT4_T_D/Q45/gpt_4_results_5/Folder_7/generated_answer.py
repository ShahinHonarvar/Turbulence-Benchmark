
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:10].lower()
    unique_permutations = set([''.join(p) for p in permutations(s) if len(set(p)) >= 7])
    palindromes = set([word for word in unique_permutations if word == word[::-1]])
    return palindromes
