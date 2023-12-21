
from itertools import permutations


def palindromes_between_indices(string):
    english_letters = [c for c in string.lower() if c.isalpha()]
    palindromes = set()
    for perm in permutations(english_letters, 4):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes
