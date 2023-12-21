
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string if char.isalpha()]
    palindromes = set()
    
    for combination in itertools.permutations(letters, 5):
        word = ''.join(combination)
        if word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
