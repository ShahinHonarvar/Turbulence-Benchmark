
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[2:10] if c.isalpha()]
    palindromes = set()
    for p in itertools.permutations(letters, len(letters)):
        palindrome = ''.join(p)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes
