
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string if char.isalpha()]
    letters_between_indices = letters[3:8]
    if len(letters_between_indices) < 6:
        return set()
    
    palindromes = set()
    for combination in itertools.permutations(letters_between_indices):
        palindrome = ''.join(combination)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    
    return palindromes
