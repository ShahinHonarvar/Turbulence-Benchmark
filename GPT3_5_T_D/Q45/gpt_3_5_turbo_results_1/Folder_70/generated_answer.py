
from itertools import permutations

def palindromes_between_indices(string):
    english_letters = [char for char in string if char.isalpha()]
    english_letters = english_letters[1:7]
    english_letters = [letter.lower() for letter in english_letters]
    palindromes = set()
    
    for permutation in permutations(english_letters, len(english_letters)):
        candidate = ''.join(permutation)
        if candidate == candidate[::-1] and len(candidate) >= 4:
            palindromes.add(candidate)
    
    return palindromes
