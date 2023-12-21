
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[:7] if c.isalpha()]

    palindromes = set()
    for perm in itertools.permutations(letters):
        palindrome = ''.join(perm)
        if palindrome.lower() == palindrome.lower()[::-1] and len(palindrome) >= 5:
            palindromes.add(palindrome)

    return palindromes
