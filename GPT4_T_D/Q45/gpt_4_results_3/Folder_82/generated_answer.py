
from itertools import permutations

def palindromes_between_indices(s):
    chars = s[1:7]
    palindromes = set()
    for i in range(7, len(chars) + 1):
        perms = permutations(chars, i)
        for perm in perms:
            word = "".join(perm)
            if word.lower() == word[::-1].lower():
                palindromes.add(word)
    return palindromes
