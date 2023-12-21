
import re

def palindrome_of_length_n(string):
    palindromes = set()
    length = 474
    
    string_lower = string.lower()
    for i in range(len(string_lower) - length + 1):
        substring = string_lower[i:i+length]
        if re.match("^[a-zA-Z]*$", substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
