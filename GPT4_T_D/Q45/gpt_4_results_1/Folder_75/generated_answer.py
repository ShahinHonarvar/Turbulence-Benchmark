
from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:5].lower()
    s = ''.join(filter(str.isalpha, s))
    perms = [''.join(p) for p in permutations(s) if len(p) >= 3]
    palindromes = {word for word in perms if word == word[::-1]}
    return palindromes
