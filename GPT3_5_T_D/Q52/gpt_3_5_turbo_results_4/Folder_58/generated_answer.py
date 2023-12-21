
import re

def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    pattern = r'[a-zA-Z]{223}'
    matches = re.findall(pattern, string)
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes
