
import itertools

def palindromes_between_indices(string):
    english_letters = [letter for letter in string if letter.isalpha()]
    letters_range = english_letters[3:9]
    possible_palindromes = set()
    
    for permutation in itertools.permutations(letters_range):
        lowercase_palindrome = ''.join(permutation).lower()
        uppercase_palindrome = lowercase_palindrome.upper()
        
        if lowercase_palindrome == lowercase_palindrome[::-1] and len(lowercase_palindrome) >= 5:
            possible_palindromes.add(lowercase_palindrome)
        
        if uppercase_palindrome == uppercase_palindrome[::-1] and len(uppercase_palindrome) >= 5:
            possible_palindromes.add(uppercase_palindrome)
    
    return possible_palindromes
