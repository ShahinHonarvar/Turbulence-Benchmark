
import itertools

def is_palindrome(s):
    return s.lower() == s.lower()[::-1]

def palindromes_between_indices(string):
    letters = [char for char in string[4:8] if char.isalpha()]
    palindromes = set()
    
    for permutation in itertools.permutations(letters):
        word = ''.join(permutation)
        if len(word) >= 5 and is_palindrome(word):
            palindromes.add(word.lower())
    
    return palindromes
