
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[4:7] if c.isalpha()]
    palindromes = set()
    
    for perm in itertools.permutations(letters):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    
    return palindromes
