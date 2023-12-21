
import itertools

def palindromes_between_indices(string):
    english_letters = [letter for letter in string if letter.isalpha()]
    english_letters = [letter.lower() for letter in english_letters]
    english_letters = english_letters[2:9]
    palindromes = set()
    
    for permutation in itertools.permutations(english_letters):
        word = ''.join(permutation)
        if len(word) >= 7 and word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
