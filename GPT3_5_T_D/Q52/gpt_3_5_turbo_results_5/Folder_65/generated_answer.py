
import re

def palindrome_of_length_n(string):
    string = string.lower()
    pattern = r'[a-zA-Z]+'
    substrings = re.findall(pattern, string)
    palindromes = set()
    for substring in substrings:
        if len(substring) == 35 and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
