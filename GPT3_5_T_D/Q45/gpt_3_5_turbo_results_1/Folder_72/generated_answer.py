
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[1:8] if c.isalpha()]
    palindromes = set()
    
    for permutation in itertools.permutations(letters):
        palindrome = ''.join(permutation)
        if palindrome == palindrome[::-1] and len(palindrome) >= 6:
            palindromes.add(palindrome)
    
    return palindromes
