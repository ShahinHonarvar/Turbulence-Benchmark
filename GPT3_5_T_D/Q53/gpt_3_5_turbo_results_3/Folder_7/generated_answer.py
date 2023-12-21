
import re

def palindrome_of_length_at_least_n(string):
    pattern = re.compile('[a-zA-Z]{122,}')
    matches = pattern.findall(string)
    palindromes = set()
    for match in matches:
        if match.lower() == match.lower()[::-1]:
            palindromes.add(match.lower())
    return palindromes
