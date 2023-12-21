
from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:10].lower()
    palindromes = set()
    for i in range(5, len(s) + 1):
        perms = set(''.join(p) for p in permutations(s, i))
        for word in perms:
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
