
import itertools
import re

def palindromes_between_indices(string):
    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    
    english_letters = re.findall('[a-zA-Z]', string)
    english_letters = english_letters[2:9]
    
    if len(english_letters) < 6:
        return set()
    
    palindromes = set()
    for permutation in itertools.permutations(english_letters, len(english_letters)):
        word = ''.join(permutation)
        if is_palindrome(word) and len(word) >= 6:
            palindromes.add(word)
    
    return palindromes
