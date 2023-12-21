
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[3:9] if char.isalpha()]
    palindromes = set()
    
    for comb in itertools.permutations(letters, len(letters)):
        word = ''.join(comb)
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    
    return palindromes
