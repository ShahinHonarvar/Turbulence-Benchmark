
from itertools import permutations

def palindromes_between_indices(s):
    char_set = s[0:3].lower()
    char_permutations = [''.join(p) for p in permutations(char_set)]
    palindromes = {word for word in char_permutations if word == word[::-1] and len(word) >= 3}
    return palindromes
