
from itertools import permutations
def palindromes_between_indices(s):
    if len(set(s[2:10])) < 7:
        return set()
    else:
        all_possibilities = set(''.join(p) for p in permutations(s[2:10], 7))
        palindromes = set(word for word in all_possibilities if word.lower() == word.lower()[::-1])
        return palindromes
