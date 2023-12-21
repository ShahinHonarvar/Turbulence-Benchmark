
import itertools

def palindromes_between_indices(string):
    string = string[1:3]
    letters = [c.lower() for c in string if c.isalpha()]
    if len(letters) < 3:
        return set()
    
    palindromes = set()
    for perm in itertools.permutations(letters):
        perm = ''.join(perm)
        if perm == perm[::-1]:
            palindromes.add(perm)
    
    return palindromes
