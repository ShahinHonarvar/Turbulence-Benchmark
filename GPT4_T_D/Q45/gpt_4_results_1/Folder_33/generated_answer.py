
from itertools import permutations

def palindromes_between_indices(s):
    s = s[7:10]
    all_possibilities = [''.join(p) for p in permutations(s)]
    palindromes = set()
    for possibility in all_possibilities:
        if len(possibility) >= 4 and possibility.lower() == possibility[::-1].lower():
            palindromes.add(possibility)
    return palindromes
