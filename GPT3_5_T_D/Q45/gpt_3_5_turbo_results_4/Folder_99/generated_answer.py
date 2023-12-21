
import itertools

def palindromes_between_indices(string):
    english_letters = [c.lower() for c in string if c.isalpha()]
    english_letters = english_letters[4:9] if len(english_letters) > 9 else []
    palindromes = set()
    
    for comb in itertools.permutations(english_letters, len(english_letters)):
        palindrome = ''.join(comb)
        if palindrome == palindrome[::-1] and len(palindrome) >= 3:
            palindromes.add(palindrome)
    
    return palindromes
