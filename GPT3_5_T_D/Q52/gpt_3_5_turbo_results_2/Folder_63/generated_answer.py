
import re

def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 17):
        substr = string[i:i+18]
        if substr == substr[::-1] and re.match("^[a-zA-Z]+$", substr):
            palindromes.add(substr)
    return palindromes
