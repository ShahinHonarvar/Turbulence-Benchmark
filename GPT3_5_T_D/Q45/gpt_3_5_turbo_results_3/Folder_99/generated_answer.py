
import itertools

def palindromes_between_indices(string):
    indices = range(4, 9)
    letters = [char.lower() for char in string if char.isalpha() and char.isascii()]
    permutations = itertools.permutations(letters, len(indices))
    palindromes = set()
    
    for perm in permutations:
        if perm == perm[::-1]:
            palindromes.add("".join(perm))
    
    return palindromes
