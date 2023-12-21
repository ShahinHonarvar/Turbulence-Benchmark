
import itertools

def palindromes_between_indices(string):
    letters = [letter for letter in string[6:9] if letter.isalpha()]
    palindromes = set()
    
    for permutation in itertools.permutations(letters, len(letters)):
        word = ''.join(permutation)
        if word.lower() == word.lower()[::-1] and len(word) >= 4:
            palindromes.add(word.upper())
            
    return palindromes
