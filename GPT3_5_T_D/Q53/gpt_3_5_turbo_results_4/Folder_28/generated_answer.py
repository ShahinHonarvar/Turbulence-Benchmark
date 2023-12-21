
import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    
    for i in range(len(string)):
        for j in range(i + 42, len(string) + 1):
            substr = string[i:j]
            if substr == substr[::-1] and re.match("^[a-z]+$", substr):
                palindromes.add(substr)
    
    return palindromes
