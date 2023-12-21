
import itertools

def palindromes_between_indices(s):
    s = s[1:9]
    # Filter the string to only contain alphabets and lower-case the string
    s = "".join(ch.lower() for ch in s if ch.isalpha())
    
    def is_palindrome(palindrome):
        return palindrome == palindrome[::-1]
    
    # We will find all the permutations of length >=7 of the string
    perms = [itertools.permutations(s, r) for r in range(7, len(s)+1)]

    # We will chain all the permutations together into a single sequence
    perms = itertools.chain(*perms)
    
    # Create strings from the sequences of characters
    string_perms = ["".join(perm) for perm in perms]
    
    # keep only the palindromes
    palindromes = set(perm for perm in string_perms if is_palindrome(perm))

    return palindromes
