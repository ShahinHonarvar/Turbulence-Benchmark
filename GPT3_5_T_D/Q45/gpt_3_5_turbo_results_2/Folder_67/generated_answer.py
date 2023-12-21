
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[2:7] if char.isalpha()]
    if len(letters) < 5:
        return set()
    
    palindromes = set()
    for perm in itertools.permutations(letters, 5):
        palindrome = ''.join(perm)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    
    return palindromes
