
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[5:10] if c.isalpha()]
    palindromes = set()
    
    for perm in itertools.permutations(letters):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    
    return palindromes
