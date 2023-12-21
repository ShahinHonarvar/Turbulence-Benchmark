
from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:10].lower()
    valid_letters = [c for c in s if c.isalpha()]
    perms = [''.join(p) for p in permutations(valid_letters) if len(p) >= 4]
    palindromes = set()
    for word in perms:
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes
