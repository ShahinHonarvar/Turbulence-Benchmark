
import re

def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 474):
        substr = string[i:i+475]
        if re.match('^[a-z]+$', substr):
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
