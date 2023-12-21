
from itertools import permutations

def palindromes_between_indices(s):
    s = s[:9].lower()
    all_permutations = [''.join(p) for p in permutations(s) if len(p) >= 7]
    possible_palindromes = set()
    for word in all_permutations:
        if word == word[::-1]:
            possible_palindromes.add(word)
    return possible_palindromes
