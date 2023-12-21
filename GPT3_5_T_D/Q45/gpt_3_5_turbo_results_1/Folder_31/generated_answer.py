 
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[1:9] if char.isalpha()]
    permutations = list(itertools.permutations(letters))
    palindromes = set()
    
    for perm in permutations:
        palindrome = ''.join(perm) + ''.join(reversed(perm))
        if len(palindrome) >= 6:
            palindromes.add(palindrome)
    
    return palindromes
