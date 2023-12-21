
from itertools import permutations

def palindromes_between_indices(string):
    string = string[0:4].lower()
    unique_perms = set(permutations(string))
    palindromes = set()
    
    for perm in unique_perms:
        possible_palindrome = ''.join(perm)
        if possible_palindrome == possible_palindrome[::-1] and len(possible_palindrome) >= 3:
            palindromes.add(possible_palindrome)
            
    return palindromes
