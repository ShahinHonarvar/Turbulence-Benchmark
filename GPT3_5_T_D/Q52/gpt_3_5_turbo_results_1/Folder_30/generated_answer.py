
import re

def palindrome_of_length_n(string):
    palindromes = set()
    length = 94

    for i in range(len(string) - length + 1):
        substr = string[i:i+length].lower()
        if substr == substr[::-1] and re.match('^[a-zA-Z]+$', substr):
            palindromes.add(substr)

    return palindromes
