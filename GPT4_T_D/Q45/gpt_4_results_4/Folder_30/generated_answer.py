
from itertools import permutations

def palindromes_between_indices(s):
    subset = s[:5]
    perms = [''.join(p) for p in permutations(subset)]
    palindromes = set()
    for word in perms:
        if len(word) >= 4 and word.lower() == word[::-1].lower():
            palindromes.add(word.lower())
    return palindromes
