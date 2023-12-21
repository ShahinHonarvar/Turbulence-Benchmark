
import itertools

def palindromes_between_indices(string):
    english_letters = [c.lower() for c in string if c.isalpha()]
    permutations = set(itertools.permutations(english_letters, 5))
    palindromes = set()
    
    for p in permutations:
        if p == p[::-1]:
            palindromes.add(''.join(p).lower())
    
    return palindromes
