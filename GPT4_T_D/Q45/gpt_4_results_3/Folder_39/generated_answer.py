
from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:6].lower()
    palindromes = set()
    for i in range(3, len(s) + 1):
        for permut in permutations(s, i):
            word = ''.join(permut)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
