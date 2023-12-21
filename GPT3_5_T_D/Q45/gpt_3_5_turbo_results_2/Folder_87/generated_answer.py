
import itertools

def palindromes_between_indices(string):
    letters = [ch.lower() for ch in string if ch.isalpha()]
    palindromes = set()
    
    for perm in itertools.permutations(letters[3:10], 3):
        palindrome = ''.join(perm) + ''.join(perm[::-1])
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    
    return palindromes
