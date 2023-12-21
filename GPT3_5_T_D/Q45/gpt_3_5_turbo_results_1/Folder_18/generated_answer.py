
from itertools import permutations

def palindromes_between_indices(string):
    english_letters = [ch for ch in string if ch.isalpha()]
    english_letters = english_letters[1:7]
    english_letters = ''.join(english_letters)
    
    palindromes = set()
    for p in permutations(english_letters):
        word = ''.join(p).lower()
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    
    return palindromes
