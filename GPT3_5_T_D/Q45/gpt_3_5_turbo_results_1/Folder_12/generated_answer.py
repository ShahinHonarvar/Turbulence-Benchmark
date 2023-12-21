
import itertools

def palindromes_between_indices(string):
    letters = [char for char in string if char.isalpha()]
    letters = letters[3:9]
    palindromes = set()
    
    for perm in itertools.permutations(letters):
        word = ''.join(perm).lower()
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
        
    return palindromes
