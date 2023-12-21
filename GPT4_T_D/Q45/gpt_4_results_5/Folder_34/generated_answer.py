
from itertools import permutations

def palindromes_between_indices(s):
    letters = s[5:8].lower()
    perms = [''.join(p) for p in permutations(letters) if len(p) >= 4]
    return set(filter(lambda x: x == x[::-1], perms))
