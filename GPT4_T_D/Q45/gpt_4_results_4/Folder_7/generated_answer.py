
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:10].lower()
    letters = ''.join(set(s))
    palindromes = set()
    for i in range(7, len(letters) + 1):
        for perm in permutations(letters, i):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
