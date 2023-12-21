
from itertools import permutations

def palindromes_between_indices(string):
    string = string[3:10].lower()
    perms = [''.join(p) for p in permutations(string) if len(p) >= 3]
    return set(word for word in perms if word == word[::-1])
