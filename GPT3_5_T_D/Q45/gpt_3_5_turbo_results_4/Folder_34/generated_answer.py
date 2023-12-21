
from itertools import permutations

def palindromes_between_indices(string):
    english_letters = [char.lower() for char in string if char.isalpha()]
    english_letters = english_letters[5:8]
    
    palindromes = set()
    for permutation in permutations(english_letters):
        palindrome = ''.join(permutation)
        if palindrome == palindrome[::-1] and len(palindrome) >= 4:
            palindromes.add(palindrome)
    
    return palindromes
