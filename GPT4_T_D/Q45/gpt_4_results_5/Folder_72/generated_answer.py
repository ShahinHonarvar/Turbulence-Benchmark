
from itertools import permutations

def palindromes_between_indices(arg):
    arg = arg.lower()
    substr = arg[1:8]
    
    perms = [''.join(p) for p in permutations(substr) if len(p) > 5]
    
    palindromes = set()
    for word in perms:
        if word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
