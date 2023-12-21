
from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:9].lower()
    potential_palindromes = set([''.join(p) for p in permutations(s) if len(p) >= 4])
    actual_palindromes = set([word for word in potential_palindromes if word == word[::-1]])
    return actual_palindromes
