
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[5:8] if c.isalpha()]
    palindromes = set()
    
    for perm in itertools.permutations(letters):
        palindrome = ''.join(perm)
        if palindrome == palindrome[::-1] and len(palindrome) >= 3:
            palindromes.add(palindrome)
    
    return palindromes
