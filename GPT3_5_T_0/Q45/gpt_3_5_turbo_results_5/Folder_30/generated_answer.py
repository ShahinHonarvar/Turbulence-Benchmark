
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string if c.isalpha()]
    palindromes = set()
    
    for combination in itertools.permutations(letters, 5):
        word = ''.join(combination)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    
    return palindromes
