
import re

def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    pattern = re.compile(r'[a-zA-Z]+')
    substrings = re.findall(pattern, string)

    for substring in substrings:
        if len(substring) == 116 and substring == substring[::-1]:
            palindromes.add(substring)

    return palindromes
