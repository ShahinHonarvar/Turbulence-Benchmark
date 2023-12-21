
import itertools
import re

def palindromes_between_indices(string):
    english_letters = re.findall(r'[a-zA-Z]', string)
    permutations = itertools.permutations(english_letters[:7])
    palindromes = set()

    for perm in permutations:
        palindrome = ''.join(perm).lower()
        if palindrome == palindrome[::-1] and len(palindrome) >= 7:
            palindromes.add(palindrome)

    return palindromes
