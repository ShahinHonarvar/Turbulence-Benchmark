
from itertools import permutations

def palindromes_between_indices(s):
    s = s[:6].lower()
    chars = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(3, len(chars) + 1):
        for perm in permutations(chars, i):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
