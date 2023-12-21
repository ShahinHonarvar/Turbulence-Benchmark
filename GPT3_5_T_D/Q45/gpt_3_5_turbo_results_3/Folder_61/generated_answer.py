
import itertools

def palindromes_between_indices(string):
    english_letters = [c for c in string if c.isalpha()]
    palindromes = set()
    
    for combination in itertools.permutations(english_letters, 7):
        palindrome = ''.join(combination).lower()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    
    return palindromes
