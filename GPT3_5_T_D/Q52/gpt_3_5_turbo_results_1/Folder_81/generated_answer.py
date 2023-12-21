
import re

def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 98):
        substr = string[i:i + 99]
        if substr == substr[::-1] and re.match("^[a-zA-Z]+$", substr):
            palindromes.add(substr)
    return palindromes
