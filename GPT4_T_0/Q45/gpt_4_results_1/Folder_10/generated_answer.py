
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    s = s[0:6]
    palindromes = set()
    for i in range(3, len(s) + 1):
        for perm in permutations(s, i):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
