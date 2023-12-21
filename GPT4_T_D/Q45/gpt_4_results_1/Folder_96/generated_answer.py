
from itertools import permutations

def palindromes_between_indices(s):
    letters = s[3:9].lower()
    all_perms = set([''.join(perms) for perms in permutations(letters)])
    palindromes = set([word for word in all_perms if word == word[::-1] and len(word) >= 6])
    return palindromes
