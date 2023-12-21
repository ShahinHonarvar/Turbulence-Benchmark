
import itertools

def palindromes_between_indices(string):
    string = string.lower()
    substr = string[2:9]
    letters = [c for c in substr if c.isalpha()]
    
    if len(letters) < 4:
        return set()
    
    palindromes = set()
    for perm in itertools.permutations(letters):
        perm = ''.join(perm)
        if perm == perm[::-1]:
            palindromes.add(perm)
    
    return palindromes
