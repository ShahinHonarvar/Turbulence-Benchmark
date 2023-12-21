
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[:6] if c.isalpha()]
    palindromes = set()
    
    if len(letters) < 5:
        return palindromes
    
    for combination in itertools.permutations(letters, len(letters)):
        word = ''.join(combination)
        
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    
    return palindromes
