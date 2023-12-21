
from itertools import permutations

def palindromes_between_indices(s):
    letters = s[0:6].lower()
    all_possibilities = set(''.join(p) for p in permutations(letters) if len(p) >= 3)
    palindromes = set(p for p in all_possibilities if p == p[::-1])
    return palindromes
