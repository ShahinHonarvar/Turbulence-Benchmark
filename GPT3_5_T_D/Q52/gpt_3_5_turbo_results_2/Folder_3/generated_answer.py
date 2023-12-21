
import re

def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    pattern = '[a-z]{100}'
    substrings = re.findall(pattern, string)
    for substring in substrings:
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
