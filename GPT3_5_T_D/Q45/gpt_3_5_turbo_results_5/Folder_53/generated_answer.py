
import itertools

def palindromes_between_indices(string):
    letters = [c for c in string.lower() if c.isalpha()]
    indices = range(4, 9)
    substrings = [''.join(substring) for substring in itertools.permutations(letters, 5)]
    palindromes = set()
    for substring in substrings:
        palindrome = substring + substring[::-1]
        if len(palindrome) >= 6:
            palindromes.add(palindrome)
    return palindromes
