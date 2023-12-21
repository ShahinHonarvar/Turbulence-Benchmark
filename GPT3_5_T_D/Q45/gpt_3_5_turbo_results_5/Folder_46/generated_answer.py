
import itertools

def palindromes_between_indices(string):
    substr = string[4:10]
    letters = [c.lower() for c in substr if c.isalpha()]
    palindromes = set()
    for perm in itertools.permutations(letters, len(letters)):
        palindrome = ''.join(perm)
        if palindrome == palindrome[::-1] and len(palindrome) >= 6:
            palindromes.add(palindrome)
    return palindromes
