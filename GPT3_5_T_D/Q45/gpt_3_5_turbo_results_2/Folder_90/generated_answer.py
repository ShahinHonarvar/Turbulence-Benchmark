
import itertools

def palindromes_between_indices(string):
    english_letters = [c for c in string if c.isalpha()]
    english_letters = ''.join(english_letters).lower()
    english_letters = english_letters[:6]
    palindromes = set()
    for combination in itertools.permutations(english_letters, len(english_letters)):
        word = ''.join(combination)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes
