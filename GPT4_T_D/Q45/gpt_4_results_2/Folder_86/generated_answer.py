
from itertools import permutations

def palindromes_between_indices(s):
    s = s[6:10].lower()
    permutations_set = set(''.join(p) for p in permutations(s) if len(p) > 3)
    palindromes = {word for word in permutations_set if word == word[::-1]}
    return palindromes
