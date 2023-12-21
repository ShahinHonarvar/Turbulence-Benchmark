
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    char_between_indices = s[1:9]
    palindromes = set()
    for n in range(7, len(char_between_indices) + 1):
        for perm in permutations(char_between_indices, n):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
