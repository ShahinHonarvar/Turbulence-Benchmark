
from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:10].lower()
    palindromes = set()
    for i in range(5, len(s) + 1):
        for perm in permutations(s, i):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
