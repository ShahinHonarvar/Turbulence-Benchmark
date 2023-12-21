
from itertools import permutations

def palindromes_between_indices(s):
    chars = s[3:6].lower()
    perms = [''.join(p) for p in permutations(chars)]
    return set(word for word in perms if word == word[::-1] and len(word) >= 4)
