
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string if char.isalpha()]
    palindromes = set()
    
    for combination in itertools.permutations(letters, 9):
        palindrome = ''.join(combination)
        if palindrome == palindrome[::-1] and len(palindrome) >= 7:
            palindromes.add(palindrome)
    
    return palindromes
