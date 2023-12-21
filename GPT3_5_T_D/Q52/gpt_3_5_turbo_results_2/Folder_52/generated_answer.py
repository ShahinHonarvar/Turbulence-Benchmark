
import re

def palindrome_of_length_n(string):
    palindromes = set()
    length = 423
    if length > len(string):
        return palindromes
    
    for i in range(len(string) - length + 1):
        substring = string[i:i+length]
        if re.match(r'^[a-zA-Z]+$', substring):
            if substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    
    return palindromes
