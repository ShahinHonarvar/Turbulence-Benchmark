
import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[3:8] if c.isalpha()]
    
    if len(letters) < 6:
        return set()
    
    palindromes = set()
    for perm in itertools.permutations(letters, 6):
        palindrome = ''.join(perm)
        if palindrome.lower() == palindrome.lower()[::-1]:
            palindromes.add(palindrome.lower())
    
    return palindromes
