
import itertools

def palindromes_between_indices(string: str) -> set:
    english_letters = [c for c in string if c.isalpha()]
    english_letters = [c.lower() for c in english_letters]
    english_letters = english_letters[1:8]
    
    palindromes = set()
    for permutation in itertools.permutations(english_letters):
        word = ''.join(permutation)
        if word == word[::-1]:
            palindromes.add(word)
            
    return palindromes
