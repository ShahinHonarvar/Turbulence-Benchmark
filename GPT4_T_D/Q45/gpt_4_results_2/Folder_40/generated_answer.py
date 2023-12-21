
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    s = s[4:10]
    if len(s) < 7:
        return set()
    perms = {''.join(p) for p in permutations(s)}
    return {word for word in perms if word == word[::-1]}
