
from itertools import permutations

def palindromes_between_indices(string):
    subset = string[0:4]
    perms = [''.join(p) for p in permutations(subset) if len(p) >= 3]
    palindromes = set()
    for word in perms:
        if word.lower() == word[::-1].lower():
            palindromes.add(word)
    return palindromes
