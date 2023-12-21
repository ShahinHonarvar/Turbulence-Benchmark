
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:9].lower()
    palindromes = set()
    for i in range(6, len(s) + 1):
        for permutation in permutations(s, i):
            word = ''.join(permutation)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
