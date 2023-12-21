
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[4:10] if char.isalpha()]
    palindromes = set()
    
    for combo in itertools.permutations(letters, len(letters)):
        word = ''.join(combo)
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    
    return palindromes
