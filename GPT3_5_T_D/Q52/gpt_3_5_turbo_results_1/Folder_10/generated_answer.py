
import re

def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - 53):
        substr = string[i:i+54]
        if re.match("^[a-zA-Z]+$", substr):
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
