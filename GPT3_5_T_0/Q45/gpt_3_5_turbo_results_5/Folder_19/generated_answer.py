
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string if c.isalpha()]
    palindromes = set()
    
    for combination in itertools.permutations(letters, 7):
        word = ''.join(combination)
        if word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
