
from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:8].lower()
    perms = [''.join(p) for p in permutations(s)]

    def is_palindrome(s):
        return s == s[::-1]
    
    palindromes = set()
    for perm in perms:
        if len(perm) >= 4 and is_palindrome(perm):
            palindromes.add(perm)

    return palindromes
