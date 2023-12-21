
import re

def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()

    for i in range(len(string)-16):
        substr = string[i:i+17]
        if substr == substr[::-1] and re.fullmatch("[a-zA-Z]+", substr):
            palindromes.add(substr)

    return palindromes
