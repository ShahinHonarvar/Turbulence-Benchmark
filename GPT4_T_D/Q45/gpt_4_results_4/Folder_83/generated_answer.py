
from itertools import permutations

def palindromes_between_indices(strng):
    substrng = strng[2:10].lower()
    perms = [''.join(p) for p in permutations(substrng) if len(p) >= 7]
    palindromes = set(word for word in perms if word == word[::-1])
    return palindromes
