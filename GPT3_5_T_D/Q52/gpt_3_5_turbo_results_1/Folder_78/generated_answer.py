
import re

def palindrome_of_length_n(string):
    set_of_palindromes = set()
    string = string.lower()
    pattern = r'[a-zA-Z]{48}'
    matches = re.findall(pattern, string)
    for match in matches:
        if match == match[::-1]:
            set_of_palindromes.add(match)
    return set_of_palindromes
