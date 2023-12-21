
import re

def palindrome_of_length_n(string):
    palindromes = set()
    length = 392
    pattern = re.compile(r'(?=(\b\w{%d}\b))' % length, re.IGNORECASE)
    matches = pattern.findall(string)
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes
