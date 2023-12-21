
from itertools import permutations

def palindromes_between_indices(s):
    substring = s[5:7]
    letters = [char.lower() for char in substring if char.isalpha()]
    potential_palindromes = {''.join(p) for p in permutations(letters) if len(p) >= 3}
    return {p for p in potential_palindromes if p == p[::-1]}
