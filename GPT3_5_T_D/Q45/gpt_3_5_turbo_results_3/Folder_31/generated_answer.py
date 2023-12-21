
from itertools import permutations

def palindromes_between_indices(string):
    english_letters = [char for char in string if char.isalpha()]
    english_letters_lower = ''.join(english_letters).lower()
    permutations_set = set(''.join(p) for p in permutations(english_letters_lower, 8))
    
    palindromes = set()
    for word in permutations_set:
        if len(word) >= 6 and word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
