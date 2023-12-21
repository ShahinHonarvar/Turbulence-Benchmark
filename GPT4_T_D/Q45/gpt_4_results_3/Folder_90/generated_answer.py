
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    characters = s[0:6]
    permutations_list = [''.join(p) for p in permutations(characters) if len(p) >= 4]
    palindromes = {p for p in permutations_list if p == p[::-1]}
    return palindromes
