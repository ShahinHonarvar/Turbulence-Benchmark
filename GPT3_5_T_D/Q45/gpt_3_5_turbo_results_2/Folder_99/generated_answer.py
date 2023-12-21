
import itertools

def palindromes_between_indices(string):
    english_letters = [char.lower() for char in string if char.isalpha()]
    english_letters_range = english_letters[4:9]
    palindromes = set()
    
    for perm in itertools.permutations(english_letters_range, len(english_letters_range)):
        palindrome = ''.join(perm)
        if palindrome.lower() == palindrome.lower()[::-1]:
            palindromes.add(palindrome)
    
    return palindromes if len(palindromes) != 0 else set()
