
import itertools

def palindromes_between_indices(string):
    english_letters = [char for char in string if char.isalpha()]
    english_letters = [char.lower() for char in english_letters]
    english_letters = english_letters[:3]
    
    permutations = itertools.permutations(english_letters)
    palindromes = set()
    
    for perm in permutations:
        palindrome = ''.join(perm)
        if palindrome == palindrome[::-1] and len(palindrome) >= 3:
            palindromes.add(palindrome)
    
    return palindromes
