
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string if c.isalpha()]
    possibilities = set(itertools.permutations(letters, 6))
    palindromes = set()
    
    for p in possibilities:
        palindrome = ''.join(p)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    
    return palindromes
