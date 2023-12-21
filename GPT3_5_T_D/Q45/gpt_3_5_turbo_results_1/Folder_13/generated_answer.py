
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string if char.isalpha()]
    letters = letters[3:10]
    permutations = set(itertools.permutations(letters))
    palindromes = set()
    
    for perm in permutations:
        if perm == perm[::-1] and len(set(perm)) >= 2:
            palindromes.add(''.join(perm))
    
    return palindromes
