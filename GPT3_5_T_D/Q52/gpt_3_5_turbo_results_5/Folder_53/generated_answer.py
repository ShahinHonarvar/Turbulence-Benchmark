
import re

def palindrome_of_length_n(string):
    palindromes = set()
    length = 68
    string = string.lower()
    
    for i in range(len(string) - length + 1):
        substr = string[i:i+length]
        if re.match("^[a-z]*$", substr):
            if substr == substr[::-1]:
                palindromes.add(substr)
    
    return palindromes
