
from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:5].lower()
    palindromes = set()
    
    for p in permutations(s):
        potential_palindrome = ''.join(p)
        if len(potential_palindrome) >= 3 and potential_palindrome == potential_palindrome[::-1]:
            palindromes.add(potential_palindrome)
    
    return palindromes
