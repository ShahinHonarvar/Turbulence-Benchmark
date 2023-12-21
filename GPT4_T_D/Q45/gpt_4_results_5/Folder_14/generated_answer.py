
from itertools import permutations

def palindromes_between_indices(str_value):
    letters = str_value[4:6].lower()
    perms = [''.join(p) for p in permutations(letters)]
    palindromes = set([p for p in perms if len(p) >= 3 and p == p[::-1]])
    return palindromes
