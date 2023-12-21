
import itertools

def palindromes_between_indices(string):
    english_letters = [char for char in string if char.isalpha()]
    english_letters = english_letters[:7]

    palindromes = set()
    for combination in itertools.permutations(english_letters, len(english_letters)):
        word = ''.join(combination).lower()
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    
    return palindromes
