
import re

def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - 23):
        substr = string[i:i+24]
        if substr == substr[::-1] and re.match("[a-zA-Z]+", substr):
            palindromes.add(substr)
    return palindromes
