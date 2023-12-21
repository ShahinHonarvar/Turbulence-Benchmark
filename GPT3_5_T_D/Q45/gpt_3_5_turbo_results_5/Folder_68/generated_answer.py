
from itertools import permutations

def palindromes_between_indices(string):
    indices_range = string[1:9]
    english_letters = [c.lower() for c in string if c.lower().isalpha()]
    palindromes = set()
    for perm in permutations(english_letters, len(indices_range)):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes
