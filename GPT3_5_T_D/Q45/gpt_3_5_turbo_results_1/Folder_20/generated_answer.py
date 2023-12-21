
import itertools

def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    perm = set(itertools.permutations(letters, 7))
    palindromes = set()
    
    for p in perm:
        word = ''.join(p).lower()
        if word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
