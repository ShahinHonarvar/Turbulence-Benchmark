
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[4:10] if c.isalpha()]
    palindromes = set()
    
    for perm in itertools.permutations(letters):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 5:
            palindromes.add(candidate)
    
    return palindromes
