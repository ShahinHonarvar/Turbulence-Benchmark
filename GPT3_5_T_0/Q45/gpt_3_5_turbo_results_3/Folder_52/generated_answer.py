
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[:8] if c.isalpha()]
    palindromes = set()
    
    for perm in itertools.permutations(letters, len(letters)):
        word = ''.join(perm)
        if len(word) >= 6 and word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
