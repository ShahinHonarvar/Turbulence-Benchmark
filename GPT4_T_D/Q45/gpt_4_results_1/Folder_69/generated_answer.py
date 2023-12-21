
from itertools import permutations

def palindromes_between_indices(string):
    substring = string[0:4].lower()
    all_permutations = [''.join(p) for p in permutations(substring)]
    palindromes = set()
    for word in all_permutations:
        if len(word) >= 4 and word == word[::-1]:
            palindromes.add(word)
    return palindromes
