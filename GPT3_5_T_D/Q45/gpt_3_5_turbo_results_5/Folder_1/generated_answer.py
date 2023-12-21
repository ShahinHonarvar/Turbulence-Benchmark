
from itertools import permutations

def palindromes_between_indices(string):
    if len(string) < 8:
        return set()
    
    substring = string[4:8]
    
    letters = [c.lower() for c in substring if c.isalpha()]
    
    if len(letters) < 5:
        return set()
    
    palindromes = set()
    
    for perm in permutations(letters, 5):
        palindrome = ''.join(perm) + ''.join(reversed(perm))
        palindromes.add(palindrome.lower())
    
    return palindromes
