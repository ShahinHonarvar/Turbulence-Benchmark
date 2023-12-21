
import itertools

def palindromes_between_indices(s):
    letters = [c.upper() for c in s[3:6] if c.isalpha()]
    palindromes = set()
    for p in itertools.permutations(letters, len(letters)):
        palindrome = ''.join(p)
        if palindrome == palindrome[::-1] and len(palindrome) >= 4:
            palindromes.add(palindrome.lower())
    return palindromes
