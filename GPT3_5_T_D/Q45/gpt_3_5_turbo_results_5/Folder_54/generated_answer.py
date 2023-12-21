
import itertools

def palindromes_between_indices(string):
    letters = [c for c in string.lower() if c.isalpha()]
    perms = list(itertools.permutations(letters, 6))
    palindromes = set()
    
    for perm in perms:
        if perm == perm[::-1]:
            palindromes.add(''.join(perm))
    
    return palindromes
