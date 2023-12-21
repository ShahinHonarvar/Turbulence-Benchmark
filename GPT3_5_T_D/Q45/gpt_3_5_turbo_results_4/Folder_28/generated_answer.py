
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string if c.isalpha()]
    palindromes = set()
    
    for p in itertools.permutations(letters, 5):
        palindrome = ''.join(p)
        palindrome_rev = ''.join(p[::-1])
        
        if palindrome == palindrome_rev and len(palindrome) >= 4:
            palindromes.add(palindrome)
    
    return palindromes
