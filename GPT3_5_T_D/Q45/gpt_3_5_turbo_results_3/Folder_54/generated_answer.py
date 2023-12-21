
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string if char.isalpha()]
    palindromes = set()
    
    for perm in itertools.permutations(letters[4:10], 6):
        palindrome = ''.join(perm)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    
    return palindromes
