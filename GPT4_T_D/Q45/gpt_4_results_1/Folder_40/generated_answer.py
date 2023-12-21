
from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:10].lower()
    s = [c for c in s if c.isalpha()]
    palindromes = set()

    for l in range(7, len(s) + 1):
        for p in permutations(s, l):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)

    return palindromes
