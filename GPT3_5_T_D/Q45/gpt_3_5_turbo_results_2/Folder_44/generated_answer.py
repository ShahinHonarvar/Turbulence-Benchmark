
import itertools

def palindromes_between_indices(string):
    string = string.lower()
    letters = [c for c in string[2:8] if c.isalpha()]
    palindromes = set()
    
    for combo in itertools.permutations(letters, len(letters)):
        word = ''.join(combo)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    
    return palindromes
