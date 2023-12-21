
import itertools

def palindromes_between_indices(string):
    letters = [char for char in string.lower() if char.isalpha()]
    palindromes = set()
    
    for arr in itertools.permutations(letters, 4):
        palindrome = ''.join(arr)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome.lower())
    
    return palindromes
