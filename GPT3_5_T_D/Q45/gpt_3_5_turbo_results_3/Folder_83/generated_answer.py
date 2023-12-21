
import itertools

def palindromes_between_indices(string):
    letters = [ch for ch in string[2:10] if ch.isalpha()]
    palindromes = set()
    
    for arrangement in itertools.permutations(letters, len(letters)):
        palindrome = ''.join(arrangement).lower()
        if palindrome == palindrome[::-1] and len(palindrome) >= 7:
            palindromes.add(palindrome)
    
    return palindromes
