
import itertools

def palindromes_between_indices(string):
    subset = string[4:7]
    letters = [letter.lower() for letter in subset if letter.isalpha()]
    palindromes = set()
    
    for combination in itertools.permutations(letters, len(letters)):
        word = ''.join(combination)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    
    return palindromes
