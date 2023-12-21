
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string if c.isalpha()]
    palindromes = set()
    
    for combination in itertools.permutations(letters, 7):
        palindrome = ''.join(combination)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    
    return palindromes
