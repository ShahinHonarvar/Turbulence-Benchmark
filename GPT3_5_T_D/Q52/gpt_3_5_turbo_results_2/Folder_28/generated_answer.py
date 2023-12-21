
import re

def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    length = 43

    for i in range(len(string) - length + 1):
        substr = string[i:i + length]
        if re.match(r'^[a-zA-Z]+$', substr):
            if substr == substr[::-1]:
                palindromes.add(substr)

    return palindromes
