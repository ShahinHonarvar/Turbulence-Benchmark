
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[4:7] if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for perm in itertools.permutations(letters):
        palindrome = ''.join(perm)
        if palindrome.lower() == palindrome.lower()[::-1]:
            palindromes.add(palindrome)
    return palindromes
