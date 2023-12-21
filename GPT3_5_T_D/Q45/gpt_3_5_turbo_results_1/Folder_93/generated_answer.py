
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string if char.isalpha()]
    indices = letters[2:8]
    palindromes = set()
    
    for combination in itertools.permutations(indices, len(indices)):
        word = ''.join(combination)
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    
    return palindromes
