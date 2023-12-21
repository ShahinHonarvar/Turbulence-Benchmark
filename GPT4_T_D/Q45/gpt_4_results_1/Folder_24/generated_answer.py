
from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:10].lower()
    palindromes = set()
    for j in range(4, len(s) + 1):
        for p in permutations(s, j):
            word = "".join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
