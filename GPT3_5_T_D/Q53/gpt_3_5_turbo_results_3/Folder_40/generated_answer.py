
import re

def palindrome_of_length_at_least_n(string):
    pattern = re.compile(r'\b\w{3,}\b')
    matches = re.findall(pattern, string.lower())
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes
