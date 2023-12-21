
from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:8].lower()
    palindromes = set()
    letters = [c for c in s if c.isalpha()]
    for n in range(6, len(letters) + 1):
        for p in permutations(letters, n):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
