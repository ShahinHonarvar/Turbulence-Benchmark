
import re

def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    
    for i in range(len(string)):
        substr = string[i:i+99]
        if len(substr) < 99:
            break
        if re.match("^[a-zA-Z]*$", substr) and substr == substr[::-1]:
            palindromes.add(substr)
    
    return palindromes
