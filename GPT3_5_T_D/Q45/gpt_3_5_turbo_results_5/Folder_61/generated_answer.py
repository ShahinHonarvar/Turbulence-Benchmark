
import itertools

def palindromes_between_indices(string):
    substrings = set()
    letters = ''.join([c for c in string.lower() if c.isalpha()])
    for combination in itertools.permutations(letters[:8], 8):
        substring = ''.join(combination).lower()
        if substring == substring[::-1] and len(substring) >= 7:
            substrings.add(substring)
    return substrings
