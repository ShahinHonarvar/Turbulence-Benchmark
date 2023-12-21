
from itertools import permutations

def palindromes_between_indices(s):
    letters = list(s[1:5].lower())
    perms = [''.join(p) for p in permutations(letters) if len(p) >= 3]
    return set(filter(lambda x: x == x[::-1], perms))
