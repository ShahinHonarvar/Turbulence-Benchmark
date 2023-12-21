
import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    
    for i in range(len(string)-44):
        for j in range(i+45, len(string)+1):
            substr = string[i:j]
            if re.match("^[a-zA-Z]+$", substr) and substr == substr[::-1]:
                palindromes.add(substr)
    
    return palindromes
