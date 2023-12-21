
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[:8] if c.isalpha()]
    permutations = list(itertools.permutations(letters, len(letters)))
    palindromes = set()
    
    for permutation in permutations:
        word = ''.join(permutation)
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    
    return palindromes
