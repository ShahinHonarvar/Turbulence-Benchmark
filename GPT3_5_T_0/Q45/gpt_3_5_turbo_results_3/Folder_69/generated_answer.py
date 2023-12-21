
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[:4] if c.isalpha()]
    palindromes = set()
    
    for perm in itertools.permutations(letters):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    
    return palindromes
