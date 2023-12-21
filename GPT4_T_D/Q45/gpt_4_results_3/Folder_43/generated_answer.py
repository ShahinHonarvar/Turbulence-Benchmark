
from itertools import permutations

def palindromes_between_indices(s):
    chars = s[2:6].lower()
    palindromes = set()
    for perm in permutations(chars):
        word = ''.join(perm)
        if len(word) >= 4 and word == word[::-1]:
            palindromes.add(word)
    return palindromes
