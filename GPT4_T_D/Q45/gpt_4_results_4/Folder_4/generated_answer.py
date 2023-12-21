
from itertools import permutations

def palindromes_between_indices(given_string):
    string = given_string[3:10].lower()
    letters = [c for c in string if c.isalpha()]
    perms = [''.join(p) for p in permutations(letters) if len(p) >= 7]
    palindromes = {p for p in perms if p == p[::-1]}
    return palindromes
