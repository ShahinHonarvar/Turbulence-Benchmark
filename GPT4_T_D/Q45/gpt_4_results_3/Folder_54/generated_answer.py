
from itertools import permutations

def palindromes_between_indices(s):
    letters = s[4:10].lower()
    palindromes = set()
    for i in range(4, len(letters) + 1):
        perms = permutations(letters, i)
        for perm in perms:
            word = "".join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
