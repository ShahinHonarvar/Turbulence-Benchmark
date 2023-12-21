
import itertools

def palindromes_between_indices(string):
    english_letters = [c.lower() for c in string if c.isalpha()]
    english_letters = english_letters[5:10]
    palindromes = set()

    for perm in itertools.permutations(english_letters, len(english_letters)):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)

    return palindromes
