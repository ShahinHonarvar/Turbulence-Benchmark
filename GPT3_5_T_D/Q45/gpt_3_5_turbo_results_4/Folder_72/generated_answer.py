
import itertools

def palindromes_between_indices(string):
    string = string.lower()
    
    letters = [char for char in string if char.isalpha()]
    letters = letters[1:8]
    
    palindromes = set()
    
    for perm in itertools.permutations(letters):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    
    return palindromes
